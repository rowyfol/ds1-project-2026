# Project 2

This folder has my Verilog files for the digital logic project.

## Folders

1. `full-adder` : one bit full adder
2. `4bit-full-adder` : four bit ripple carry adder
3. `2-1-mux` : one bit 2 to 1 multiplexer
4. `4bit-mux` : four bit 2 to 1 multiplexer
5. `8bit-adders` : 8 bit ripple carry adder and carry select adder
6. `report` : short LaTeX text for the simulation and delay part

## Run

Run all simulations:

```bash
make test
```

Open the 8 bit adder waveform:

```bash
make wave-adders8
```

Clean generated files:

```bash
make clean
```
