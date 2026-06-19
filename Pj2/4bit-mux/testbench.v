`timescale 1ns/1ps

module tb_main_mux;
  reg [3:0] A, B;
  reg Sel;
  wire [3:0] Y;

  mux4bit DUT(A, B, Sel, Y);

  initial begin
    $dumpfile("Pj2/4bit-mux/mux4.vcd");
    $dumpvars(0, tb_main_mux);
    $monitor("time=%0t A=%b B=%b Sel=%b  Y=%b", $time, A, B, Sel, Y);

    A = 4'b1010; B = 4'b0101; Sel = 0;
    #30;

    Sel = 1;
    #30;

    A = 4'b1111; B = 4'b0000; Sel = 0;
    #30;

    Sel = 1;
    #30;

    $finish;
  end
endmodule
