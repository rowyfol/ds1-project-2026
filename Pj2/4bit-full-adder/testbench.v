`timescale 1ns/1ps

module tb_adder4;
  reg [3:0] A, B;
  reg Cin;
  wire [3:0] S;
  wire Cout;

  adder4 DUT(A, B, Cin, S, Cout);

  initial begin
    $dumpfile("Pj2/4bit-full-adder/adder4.vcd");
    $dumpvars(0, tb_adder4);
    $monitor("time=%0t A=%b B=%b Cin=%b  S=%b Cout=%b", $time, A, B, Cin, S, Cout);

    A = 4'b0011; B = 4'b0101; Cin = 0;
    #80;

    A = 4'b1111; B = 4'b0001; Cin = 0;
    #80;

    A = 4'b1010; B = 4'b0110; Cin = 1;
    #80;

    A = 4'b1111; B = 4'b1111; Cin = 1;
    #80;

    $finish;
  end
endmodule
