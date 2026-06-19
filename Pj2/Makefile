# Project 2 Makefile
# Run from this folder: cd Pj2

IVERILOG ?= iverilog
VVP      ?= vvp
GTKWAVE  ?= gtkwave
PYTHON   ?= python3

BUILD_DIR := build
IMG_DIR   := wave-images
GTKW_DIR  := gtkw-files

FULL_ADDER_SRC := full-adder/main.v full-adder/testbench.v
MUX2_SRC       := 2-1-mux/mux_main.v 2-1-mux/testbench.v
ADDER4_SRC     := 4bit-full-adder/fulladder.v 4bit-full-adder/adder.v 4bit-full-adder/testbench.v
MUX4_SRC       := 4bit-mux/2-1_mux.v 4bit-mux/main_mux.v 4bit-mux/testbench.v
ADDERS8_SRC    := full-adder/main.v 4bit-full-adder/adder.v 4bit-mux/2-1_mux.v 4bit-mux/main_mux.v 8bit-adders/ripple_carry_adder8.v 8bit-adders/carry_select_adder8.v 8bit-adders/testbench.v

VCD_FULL_ADDER := full-adder/full_adder.vcd
VCD_MUX2       := 2-1-mux/mux2.vcd
VCD_ADDER4     := 4bit-full-adder/adder4.vcd
VCD_MUX4       := 4bit-mux/mux4.vcd
VCD_ADDERS8    := 8bit-adders/adders8.vcd

.PHONY: all help compile test full-adder mux2 adder4 mux4 adders8 images gtkw-files waves view-8bit clean

all: test

help:
	@echo "make test       : compile and run all simulations"
	@echo "make images     : create PNG waveform images from VCD files"
	@echo "make gtkw-files : create GTKWave save files (.gtkw)"
	@echo "make waves      : create both PNG images and GTKWave files"
	@echo "make view-8bit  : open 8-bit adder waveform in GTKWave"
	@echo "make clean      : remove generated files"

compile: $(BUILD_DIR)/full_adder.vvp $(BUILD_DIR)/mux2.vvp $(BUILD_DIR)/adder4.vvp $(BUILD_DIR)/mux4.vvp $(BUILD_DIR)/adders8.vvp

test: full-adder mux2 adder4 mux4 adders8

$(BUILD_DIR):
	mkdir -p $@

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

images: test
	mkdir -p $(IMG_DIR)
	$(PYTHON) tools/wave_tools.py png $(VCD_FULL_ADDER) $(IMG_DIR)/full_adder.png
	$(PYTHON) tools/wave_tools.py png $(VCD_MUX2) $(IMG_DIR)/mux2.png
	$(PYTHON) tools/wave_tools.py png $(VCD_ADDER4) $(IMG_DIR)/adder4.png
	$(PYTHON) tools/wave_tools.py png $(VCD_MUX4) $(IMG_DIR)/mux4.png
	$(PYTHON) tools/wave_tools.py png $(VCD_ADDERS8) $(IMG_DIR)/adders8.png
	@echo "PNG waveform images are in $(IMG_DIR)/"

gtkw-files: test
	mkdir -p $(GTKW_DIR)
	$(PYTHON) tools/wave_tools.py gtkw $(VCD_FULL_ADDER) $(GTKW_DIR)/full_adder.gtkw
	$(PYTHON) tools/wave_tools.py gtkw $(VCD_MUX2) $(GTKW_DIR)/mux2.gtkw
	$(PYTHON) tools/wave_tools.py gtkw $(VCD_ADDER4) $(GTKW_DIR)/adder4.gtkw
	$(PYTHON) tools/wave_tools.py gtkw $(VCD_MUX4) $(GTKW_DIR)/mux4.gtkw
	$(PYTHON) tools/wave_tools.py gtkw $(VCD_ADDERS8) $(GTKW_DIR)/adders8.gtkw
	@echo "GTKWave save files are in $(GTKW_DIR)/"

waves: images gtkw-files

view-8bit: adders8 gtkw-files
	$(GTKWAVE) $(GTKW_DIR)/adders8.gtkw

clean:
	rm -rf $(BUILD_DIR) $(IMG_DIR) $(GTKW_DIR)
	rm -f $(VCD_FULL_ADDER) $(VCD_MUX2) $(VCD_ADDER4) $(VCD_MUX4) $(VCD_ADDERS8)
