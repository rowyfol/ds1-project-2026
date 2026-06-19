module carry_select_adder8(
  input [7:0] A,
  input [7:0] B,
  input Cin,
  output [7:0] S,
  output Cout
);
  wire c4;
  wire [3:0] sum_hi_c0, sum_hi_c1;
  wire cout_hi_c0, cout_hi_c1;

  adder4 LOW(A[3:0], B[3:0], Cin, S[3:0], c4);
  adder4 HIGH_C0(A[7:4], B[7:4], 1'b0, sum_hi_c0, cout_hi_c0);
  adder4 HIGH_C1(A[7:4], B[7:4], 1'b1, sum_hi_c1, cout_hi_c1);

  mux4bit SUM_SELECT(sum_hi_c0, sum_hi_c1, c4, S[7:4]);
  mux2_to_1 COUT_SELECT(cout_hi_c0, cout_hi_c1, c4, Cout);
endmodule
