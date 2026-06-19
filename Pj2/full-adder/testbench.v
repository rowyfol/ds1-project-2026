`timescale 1ns/1ps

module tb_full_adder;
  reg A, B, Cin;
  wire S, Co;

  full_adder DUT(A, B, Cin, S, Co);

  initial begin
    $dumpfile("full-adder/full_adder.vcd");
    $dumpvars(0, tb_full_adder);
    $monitor("time=%0t A=%b B=%b Cin=%b  S=%b Co=%b", $time, A, B, Cin, S, Co);

    A = 0; B = 0; Cin = 0;
    #25;

    A = 0; B = 1; Cin = 1;
    #25;

    A = 1; B = 0; Cin = 1;
    #25;

    A = 1; B = 1; Cin = 1;
    #25;

    $finish;
  end
endmodule
