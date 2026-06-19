# Project 2 Makefile
# Usage examples:
#   make test      -> run all simulations
#   make waves     -> run all simulations and create SVG waveform images
#   make view-8bit -> open the 8-bit VCD file in GTKWave

IVERILOG ?= iverilog
VVP      ?= vvp
GTKWAVE  ?= gtkwave
PYTHON   ?= python3

BUILD_DIR := build
WAVE_DIR  := wave-images

FULL_ADDER_SRC := full-adder/main.v full-adder/testbench.v
MUX2_SRC       := 2-1-mux/mux_main.v 2-1-mux/testbench.v
ADDER4_SRC     := 4bit-full-adder/fulladder.v 4bit-full-adder/adder.v 4bit-full-adder/testbench.v
MUX4_SRC       := 4bit-mux/2-1_mux.v 4bit-mux/main_mux.v 4bit-mux/testbench.v
ADDERS8_SRC    := full-adder/main.v 4bit-full-adder/adder.v 4bit-mux/2-1_mux.v 4bit-mux/main_mux.v 8bit-adders/ripple_carry_adder8.v 8bit-adders/carry_select_adder8.v 8bit-adders/testbench.v

.PHONY: all test compile full-adder mux2 adder4 mux4 adders8 waves view-8bit clean help

all: test

help:
	@echo "Project 2 Makefile"
	@echo "  make test      compile and run all simulations"
	@echo "  make waves     run simulations and create SVG waveform images"
	@echo "  make view-8bit open the 8-bit adder waveform in GTKWave"
	@echo "  make clean     remove generated files"

compile: $(BUILD_DIR)/full_adder.vvp $(BUILD_DIR)/mux2.vvp $(BUILD_DIR)/adder4.vvp $(BUILD_DIR)/mux4.vvp $(BUILD_DIR)/adders8.vvp

test: full-adder mux2 adder4 mux4 adders8

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(WAVE_DIR):
	mkdir -p $(WAVE_DIR)

$(BUILD_DIR)/full_adder.vvp: $(FULL_ADDER_SRC) | $(BUILD_DIR)
	$(IVERILOG) -Wall -o $@ $(FULL_ADDER_SRC)

$(BUILD_DIR)/mux2.vvp: $(MUX2_SRC) | $(BUILD_DIR)
	$(IVERILOG) -Wall -o $@ $(MUX2_SRC)

$(BUILD_DIR)/adder4.vvp: $(ADDER4_SRC) | $(BUILD_DIR)
	$(IVERILOG) -Wall -o $@ $(ADDER4_SRC)

$(BUILD_DIR)/mux4.vvp: $(MUX4_SRC) | $(BUILD_DIR)
	$(IVERILOG) -Wall -o $@ $(MUX4_SRC)

$(BUILD_DIR)/adders8.vvp: $(ADDERS8_SRC) | $(BUILD_DIR)
	$(IVERILOG) -Wall -o $@ $(ADDERS8_SRC)

full-adder: $(BUILD_DIR)/full_adder.vvp
	$(VVP) $<

mux2: $(BUILD_DIR)/mux2.vvp
	$(VVP) $<

adder4: $(BUILD_DIR)/adder4.vvp
	$(VVP) $<

mux4: $(BUILD_DIR)/mux4.vvp
	$(VVP) $<

adders8: $(BUILD_DIR)/adders8.vvp
	$(VVP) $<

waves: test | $(WAVE_DIR)
	$(PYTHON) tools/vcd_to_svg.py full-adder/full_adder.vcd $(WAVE_DIR)/full_adder.svg
	$(PYTHON) tools/vcd_to_svg.py 2-1-mux/mux2.vcd $(WAVE_DIR)/mux2.svg
	$(PYTHON) tools/vcd_to_svg.py 4bit-full-adder/adder4.vcd $(WAVE_DIR)/adder4.svg
	$(PYTHON) tools/vcd_to_svg.py 4bit-mux/mux4.vcd $(WAVE_DIR)/mux4.svg
	$(PYTHON) tools/vcd_to_svg.py 8bit-adders/adders8.vcd $(WAVE_DIR)/adders8.svg
	@echo "Waveform images are in $(WAVE_DIR)/"

view-8bit: adders8
	$(GTKWAVE) 8bit-adders/adders8.vcd

clean:
	rm -rf $(BUILD_DIR) $(WAVE_DIR)
	rm -f full-adder/*.vcd 2-1-mux/*.vcd 4bit-full-adder/*.vcd 4bit-mux/*.vcd 8bit-adders/*.vcd
