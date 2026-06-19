#!/usr/bin/env python3
"""Small VCD to SVG waveform drawer for this project.

It uses only the Python standard library, so no extra package is needed.
"""

import html
import sys
from pathlib import Path

LEFT = 140
RIGHT = 30
TOP = 35
ROW_H = 42
PX_PER_STEP = 8
MIN_W = 900


def read_vcd(path):
    signals = {}
    order = []
    values = {}
    times = []
    current_time = 0
    in_header = True

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue

            if line.startswith("$enddefinitions"):
                in_header = False
                continue

            if in_header:
                if line.startswith("$var"):
                    parts = line.split()
                    if len(parts) >= 5:
                        width = int(parts[2])
                        code = parts[3]
                        name = parts[4]
                        signals[code] = {"name": name, "width": width}
                        order.append(code)
                        values[code] = [(0, "x")]
                continue

            if line.startswith("#"):
                current_time = int(line[1:])
                times.append(current_time)
                continue

            if line[0] in "01xzXZ":
                code = line[1:]
                val = line[0].lower()
                if code in values:
                    values[code].append((current_time, val))
                continue

            if line[0] in "bB":
                parts = line.split()
                if len(parts) == 2:
                    val = parts[0][1:].lower()
                    code = parts[1]
                    if code in values:
                        values[code].append((current_time, val))

    max_time = max(times) if times else 1
    return [(signals[c]["name"], signals[c]["width"], values[c]) for c in order], max_time


def digital_path(changes, max_time, xscale, y_mid):
    high = y_mid - 11
    low = y_mid + 11
    unknown = y_mid

    def y_of(v):
        if v == "1":
            return high
        if v == "0":
            return low
        return unknown

    points = []
    last_t = 0
    last_v = changes[0][1] if changes else "x"
    points.append((0, y_of(last_v)))

    for t, v in changes[1:]:
        points.append((t * xscale, y_of(last_v)))
        points.append((t * xscale, y_of(v)))
        last_t = t
        last_v = v

    points.append((max_time * xscale, y_of(last_v)))
    return " ".join(f"{LEFT + x:.1f},{y:.1f}" for x, y in points)


def draw_bus(changes, max_time, xscale, y_mid):
    parts = []
    used = []
    for i, (t, val) in enumerate(changes):
        end = changes[i + 1][0] if i + 1 < len(changes) else max_time
        if end == t:
            continue
        x1 = LEFT + t * xscale
        x2 = LEFT + end * xscale
        used.append((t, end, val, x1, x2))
        parts.append(f'<line x1="{x1:.1f}" y1="{y_mid - 10}" x2="{x2:.1f}" y2="{y_mid - 10}" stroke="#1f77b4"/>')
        parts.append(f'<line x1="{x1:.1f}" y1="{y_mid + 10}" x2="{x2:.1f}" y2="{y_mid + 10}" stroke="#1f77b4"/>')
        parts.append(f'<line x1="{x1:.1f}" y1="{y_mid - 10}" x2="{x1:.1f}" y2="{y_mid + 10}" stroke="#1f77b4"/>')
        if x2 - x1 > 32:
            label = html.escape(val)
            parts.append(f'<text x="{(x1 + x2) / 2:.1f}" y="{y_mid + 4}" text-anchor="middle" font-size="11">{label}</text>')
    if used:
        x2 = LEFT + max_time * xscale
        parts.append(f'<line x1="{x2:.1f}" y1="{y_mid - 10}" x2="{x2:.1f}" y2="{y_mid + 10}" stroke="#1f77b4"/>')
    return "\n".join(parts)


def make_svg(vcd_path, out_path):
    signals, max_time = read_vcd(vcd_path)
    # Keep project-level signals and skip tiny internal carry wires if names repeat too much.
    shown = []
    seen = set()
    for name, width, changes in signals:
        if name in seen:
            continue
        seen.add(name)
        shown.append((name, width, changes))

    width = max(MIN_W, LEFT + RIGHT + max_time * PX_PER_STEP)
    xscale = (width - LEFT - RIGHT) / max_time
    height = TOP + ROW_H * len(shown) + 45

    title = html.escape(Path(vcd_path).name)
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:monospace;} .grid{stroke:#dddddd;stroke-width:1;} .wave{fill:none;stroke:#1f77b4;stroke-width:2;}</style>',
        f'<text x="20" y="22" font-size="16">Waveform: {title}</text>',
    ]

    for i in range(6):
        t = int(max_time * i / 5)
        x = LEFT + t * xscale
        svg.append(f'<line class="grid" x1="{x:.1f}" y1="30" x2="{x:.1f}" y2="{height - 30}"/>')
        svg.append(f'<text x="{x:.1f}" y="{height - 10}" text-anchor="middle" font-size="11">{t}</text>')

    for row, (name, width_bits, changes) in enumerate(shown):
        y = TOP + row * ROW_H + 20
        svg.append(f'<text x="15" y="{y + 4}" font-size="12">{html.escape(name)}</text>')
        svg.append(f'<line class="grid" x1="{LEFT}" y1="{y + 18}" x2="{width - RIGHT}" y2="{y + 18}"/>')
        if width_bits == 1:
            svg.append(f'<polyline class="wave" points="{digital_path(changes, max_time, xscale, y)}"/>')
        else:
            svg.append(draw_bus(changes, max_time, xscale, y))

    svg.append('</svg>')
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text("\n".join(svg), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: vcd_to_svg.py input.vcd output.svg", file=sys.stderr)
        sys.exit(2)
    make_svg(sys.argv[1], sys.argv[2])
