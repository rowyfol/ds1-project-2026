#!/usr/bin/env python3
"""Create readable PNG waveform pictures and GTKWave save files from VCD."""

import os, re, struct, sys, zlib
from pathlib import Path

BG=(255,255,255); GRID=(225,225,225); BLUE=(25,92,180); BUS=(230,242,255); TXT=(20,20,20); XCOL=(220,70,60)
LEFT=170; RIGHT=35; TOP=55; ROW=58; WMIN=1200
FONT={
' ':['000','000','000','000','000','000','000'],
'A':['01110','10001','10001','11111','10001','10001','10001'],'B':['11110','10001','10001','11110','10001','10001','11110'],'C':['01111','10000','10000','10000','10000','10000','01111'],'D':['11110','10001','10001','10001','10001','10001','11110'],'E':['11111','10000','10000','11110','10000','10000','11111'],'F':['11111','10000','10000','11110','10000','10000','10000'],'G':['01111','10000','10000','10011','10001','10001','01111'],'H':['10001','10001','10001','11111','10001','10001','10001'],'I':['111','010','010','010','010','010','111'],'J':['00111','00010','00010','00010','00010','10010','01100'],'K':['10001','10010','10100','11000','10100','10010','10001'],'L':['10000','10000','10000','10000','10000','10000','11111'],'M':['10001','11011','10101','10101','10001','10001','10001'],'N':['10001','11001','10101','10011','10001','10001','10001'],'O':['01110','10001','10001','10001','10001','10001','01110'],'P':['11110','10001','10001','11110','10000','10000','10000'],'Q':['01110','10001','10001','10001','10101','10010','01101'],'R':['11110','10001','10001','11110','10100','10010','10001'],'S':['01111','10000','10000','01110','00001','00001','11110'],'T':['11111','00100','00100','00100','00100','00100','00100'],'U':['10001','10001','10001','10001','10001','10001','01110'],'V':['10001','10001','10001','10001','10001','01010','00100'],'W':['10001','10001','10001','10101','10101','10101','01010'],'X':['10001','10001','01010','00100','01010','10001','10001'],'Y':['10001','10001','01010','00100','00100','00100','00100'],'Z':['11111','00001','00010','00100','01000','10000','11111'],
'0':['01110','10001','10011','10101','11001','10001','01110'],'1':['010','110','010','010','010','010','111'],'2':['01110','10001','00001','00010','00100','01000','11111'],'3':['11110','00001','00001','01110','00001','00001','11110'],'4':['00010','00110','01010','10010','11111','00010','00010'],'5':['11111','10000','10000','11110','00001','00001','11110'],'6':['01110','10000','10000','11110','10001','10001','01110'],'7':['11111','00001','00010','00100','01000','01000','01000'],'8':['01110','10001','10001','01110','10001','10001','01110'],'9':['01110','10001','10001','01111','00001','00001','01110'],
'_':['00000','00000','00000','00000','00000','00000','11111'],'-':['00000','00000','00000','11111','00000','00000','00000'],'.':['0','0','0','0','0','0','1'],':':['0','1','0','0','0','1','0'],'/':['00001','00010','00010','00100','01000','01000','10000'],'[':['111','100','100','100','100','100','111'],']':['111','001','001','001','001','001','111']
}

def parse_vcd(path):
    scopes=[]; codes={}; order=[]; vals={}; t=0; maxt=0; header=True
    for raw in open(path, encoding='utf-8', errors='ignore'):
        s=raw.strip()
        if not s: continue
        if header:
            if s.startswith('$scope'):
                p=s.split(); scopes.append(p[2])
            elif s.startswith('$upscope'):
                if scopes: scopes.pop()
            elif s.startswith('$var'):
                p=s.split(); width=int(p[2]); code=p[3]; name=p[4]
                full='.'.join(scopes+[name]) if scopes else name
                codes[code]=(full,width); order.append(code); vals[code]=[(0,'x')]
            elif s.startswith('$enddefinitions'):
                header=False
            continue
        if s.startswith('#'):
            t=int(s[1:]); maxt=max(maxt,t); continue
        if s[0] in '01xXzZ':
            code=s[1:];
            if code in vals: vals[code].append((t,s[0].lower()))
        elif s[0] in 'bB':
            p=s.split();
            if len(p)==2 and p[1] in vals: vals[p[1]].append((t,p[0][1:].lower()))
    sig=[]; seen=set()
    for c in order:
        name,w=codes[c]
        short=name.split('.')[-1]
        if short in seen: continue
        seen.add(short); sig.append((short,w,vals[c],name))
    return sig, max(maxt,1)

def img(w,h): return [[BG for _ in range(w)] for __ in range(h)]
def pix(im,x,y,c):
    if 0<=x<len(im[0]) and 0<=y<len(im): im[y][x]=c
def line(im,x1,y1,x2,y2,c):
    x1=int(x1);y1=int(y1);x2=int(x2);y2=int(y2); dx=abs(x2-x1); dy=-abs(y2-y1); sx=1 if x1<x2 else -1; sy=1 if y1<y2 else -1; e=dx+dy
    while True:
        pix(im,x1,y1,c)
        if x1==x2 and y1==y2: break
        e2=2*e
        if e2>=dy: e+=dy; x1+=sx
        if e2<=dx: e+=dx; y1+=sy
def rect(im,x1,y1,x2,y2,c,fill=None):
    if fill:
        for y in range(max(0,int(y1)), min(len(im),int(y2)+1)):
            for x in range(max(0,int(x1)), min(len(im[0]),int(x2)+1)): im[y][x]=fill
    line(im,x1,y1,x2,y1,c); line(im,x2,y1,x2,y2,c); line(im,x2,y2,x1,y2,c); line(im,x1,y2,x1,y1,c)
def text(im,x,y,s,scale=2,c=TXT):
    x0=x
    for ch in str(s).upper():
        pat=FONT.get(ch,FONT.get(' '));
        for yy,row in enumerate(pat):
            for xx,v in enumerate(row):
                if v=='1':
                    for sy in range(scale):
                        for sx in range(scale): pix(im,x+xx*scale+sx,y+yy*scale+sy,c)
        x += (max(len(r) for r in pat)+1)*scale
    return x-x0

def save_png(path, im):
    h=len(im); w=len(im[0])
    raw=b''.join(b'\x00'+bytes([v for p in row for v in p]) for row in im)
    def chunk(t,d): return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    data=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw,9))+chunk(b'IEND',b'')
    Path(path).parent.mkdir(parents=True,exist_ok=True); Path(path).write_bytes(data)

def stable(v): return v and set(v)<=set('01')
def make_png(vcd,out):
    sig,maxt=parse_vcd(vcd); w=max(WMIN,LEFT+RIGHT+maxt*5); xs=(w-LEFT-RIGHT)/maxt; h=TOP+ROW*len(sig)+55; im=img(int(w),int(h))
    text(im,20,16,'WAVEFORM '+Path(vcd).name,2)
    for i in range(11):
        tt=int(maxt*i/10); x=int(LEFT+tt*xs); line(im,x,TOP-10,x,h-35,GRID); text(im,x-10,h-25,str(tt),1)
    for r,(name,width,changes,full_name) in enumerate(sig):
        y=TOP+r*ROW+25; text(im,15,y-8,name,2); line(im,LEFT,y+20,w-RIGHT,y+20,GRID)
        if width==1:
            hi=y-15; lo=y+15; mid=y
            def yy(v): return hi if v=='1' else lo if v=='0' else mid
            lv=changes[0][1]
            for t,v in changes[1:]+[(maxt,lv)]:
                x=int(LEFT+t*xs); lastx=int(LEFT+changes[0][0]*xs) if False else None
            last_t=0; last_v=changes[0][1]
            for t,v in changes[1:]+[(maxt,last_v)]:
                x1=int(LEFT+last_t*xs); x2=int(LEFT+t*xs); col=BLUE if stable(last_v) else XCOL
                line(im,x1,yy(last_v),x2,yy(last_v),col); line(im,x2,yy(last_v),x2,yy(v),col)
                last_t=t; last_v=v
        else:
            for i,(t,v) in enumerate(changes):
                end=changes[i+1][0] if i+1<len(changes) else maxt
                if end<=t: continue
                x1=int(LEFT+t*xs); x2=int(LEFT+end*xs); fill=BUS if stable(v) else (255,235,235)
                rect(im,x1,y-15,x2,y+15,BLUE,fill)
                if x2-x1>45: text(im,x1+5,y-5,v,1)
    save_png(out,im)

def make_gtkw(vcd,out):
    sig,_=parse_vcd(vcd)
    lines=['[dumpfile] "'+str(Path(vcd).resolve())+'"','[timestart] 0','[size] 1200 700','[sst_width] 240','@28']
    for name,_,__,full_name in sig: lines.append(full_name)
    Path(out).parent.mkdir(parents=True,exist_ok=True); Path(out).write_text('\n'.join(lines)+'\n')

def main():
    if len(sys.argv)<4 or sys.argv[1] not in ('png','gtkw'):
        print('usage: wave_tools.py png input.vcd output.png')
        print('       wave_tools.py gtkw input.vcd output.gtkw')
        sys.exit(2)
    if sys.argv[1]=='png': make_png(sys.argv[2],sys.argv[3])
    else: make_gtkw(sys.argv[2],sys.argv[3])
if __name__=='__main__': main()
