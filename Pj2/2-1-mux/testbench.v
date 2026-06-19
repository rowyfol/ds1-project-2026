module testbench;
reg I0,I1,Sel;
wire Y;
mux_main DUT(
    I0,I1,Sel,Y
);


initial begin

I0=0; I1=1; Sel=0;
#20;

I0=0; I1=1; Sel=1;
#20;

I0=1; I1=0; Sel=1;
#20;

$stop;
end
endmodule
