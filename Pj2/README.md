# Project 2

This folder has my Verilog files for the digital logic project.

## Folders

1. `full-adder` : one bit full adder
2. `4bit-full-adder` : four bit ripple carry adder
3. `2-1-mux` : one bit 2 to 1 multiplexer
4. `4bit-mux` : four bit 2 to 1 multiplexer
5. `8bit-adders` : 8 bit ripple carry adder and carry select adder
6. `report` : short LaTeX text for the simulation and delay part
7. `tools` : small script for making PNG waveform images and GTKWave files

## Run

First go to the project folder:

```bash
cd Pj2
```

Run all simulations:

```bash
make test
```

Generate PNG waveform images for all parts:

```bash
make waves
```

The images will be created in `Pj2/wave-images`. GTKWave save files can be created with `make gtkw-files` and will be placed in `Pj2/gtkw-files`.

Open the 8 bit adder waveform in GTKWave:

```bash
make view-8bit
```

Clean generated files:

```bash
make clean
```
