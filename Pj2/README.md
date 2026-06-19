# Project 2

This folder contains the Verilog files for the digital logic project.

## Folders

1. `full-adder` : one bit full adder with separate delays for sum and carry
2. `4bit-full-adder` : four bit ripple carry adder made from full adders
3. `2-1-mux` : one bit 2 to 1 multiplexer
4. `4bit-mux` : four bit 2 to 1 multiplexer made from one bit multiplexers
5. `8bit-adders` : 8 bit ripple carry adder and carry select adder
6. `report` : short LaTeX text for the simulation and delay comparison

## Run

First go to the project folder:

```bash
cd Pj2
```

Compile every simulation:

```bash
make compile
```

Run all simulations and generate VCD waveform files:

```bash
make test
```

Open the 8 bit adder waveform in GTKWave:

```bash
make view-8bit
```

Clean generated files:

```bash
make clean
```
