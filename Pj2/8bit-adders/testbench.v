`timescale 1ns/1ps

module tb_adders8;
  reg [7:0] A, B;
  reg Cin;
  wire [7:0] S_ripple, S_select;
  wire Cout_ripple, Cout_select;

  ripple_carry_adder8 RCA(A, B, Cin, S_ripple, Cout_ripple);
  carry_select_adder8 CSA(A, B, Cin, S_select, Cout_select);

  initial begin
    $dumpfile("8bit-adders/adders8.vcd");
    $dumpvars(0, tb_adders8);
    $monitor("time=%0t A=%h B=%h Cin=%b  ripple=%b_%h  select=%b_%h",
             $time, A, B, Cin, Cout_ripple, S_ripple, Cout_select, S_select);

    A = 8'h00; B = 8'h00; Cin = 0;
    #120;

    A = 8'h0f; B = 8'h01; Cin = 0;
    #120;

    A = 8'h55; B = 8'haa; Cin = 1;
    #120;

    A = 8'hff; B = 8'h01; Cin = 0;
    #120;

    A = 8'hff; B = 8'hff; Cin = 1;
    #120;

    $finish;
  end
endmodule
