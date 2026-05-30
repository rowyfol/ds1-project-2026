#!/bin/bash

echo "Compiling Verilog files..."
iverilog -o sim_output.vvp main.v testbench.v

echo "Running simulation..."
# Run the simulation and save the $monitor output to a text file
vvp sim_output.vvp | tee simulation.log

echo "Opening GTKWave..."
gtkwave wave.vcd &
