IVERILOG = iverilog
VVP = vvp
GTKWAVE = gtkwave
BUILD = build

all: test

test: full_adder mux2 adder4 mux4 adders8

full_adder:
	mkdir -p $(BUILD)
	$(IVERILOG) -o $(BUILD)/full_adder.vvp Pj2/full-adder/main.v Pj2/full-adder/testbench.v
	$(VVP) $(BUILD)/full_adder.vvp

mux2:
	mkdir -p $(BUILD)
	$(IVERILOG) -o $(BUILD)/mux2.vvp Pj2/2-1-mux/mux_main.v Pj2/2-1-mux/testbench.v
	$(VVP) $(BUILD)/mux2.vvp

adder4:
	mkdir -p $(BUILD)
	$(IVERILOG) -o $(BUILD)/adder4.vvp Pj2/4bit-full-adder/fulladder.v Pj2/4bit-full-adder/adder.v Pj2/4bit-full-adder/testbench.v
	$(VVP) $(BUILD)/adder4.vvp

mux4:
	mkdir -p $(BUILD)
	$(IVERILOG) -o $(BUILD)/mux4.vvp Pj2/4bit-mux/2-1_mux.v Pj2/4bit-mux/main_mux.v Pj2/4bit-mux/testbench.v
	$(VVP) $(BUILD)/mux4.vvp

adders8:
	mkdir -p $(BUILD)
	$(IVERILOG) -o $(BUILD)/adders8.vvp Pj2/full-adder/main.v Pj2/4bit-full-adder/adder.v Pj2/4bit-mux/2-1_mux.v Pj2/4bit-mux/main_mux.v Pj2/8bit-adders/ripple_carry_adder8.v Pj2/8bit-adders/carry_select_adder8.v Pj2/8bit-adders/testbench.v
	$(VVP) $(BUILD)/adders8.vvp

wave-adders8: adders8
	$(GTKWAVE) Pj2/8bit-adders/adders8.vcd

clean:
	rm -rf $(BUILD)
	rm -f Pj2/full-adder/*.vcd Pj2/2-1-mux/*.vcd Pj2/4bit-full-adder/*.vcd Pj2/4bit-mux/*.vcd Pj2/8bit-adders/*.vcd

.PHONY: all test full_adder mux2 adder4 mux4 adders8 wave-adders8 clean
