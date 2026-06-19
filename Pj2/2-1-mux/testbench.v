`timescale 1ns/1ps

module testbench;
  reg I0, I1, Sel;
  wire Y;

  mux_main DUT(I0, I1, Sel, Y);

  initial begin
    $dumpfile("Pj2/2-1-mux/mux2.vcd");
    $dumpvars(0, testbench);
    $monitor("time=%0t I0=%b I1=%b Sel=%b  Y=%b", $time, I0, I1, Sel, Y);

    I0 = 0; I1 = 1; Sel = 0;
    #20;

    I0 = 0; I1 = 1; Sel = 1;
    #20;

    I0 = 1; I1 = 0; Sel = 0;
    #20;

    I0 = 1; I1 = 0; Sel = 1;
    #20;

    $finish;
  end
endmodule
