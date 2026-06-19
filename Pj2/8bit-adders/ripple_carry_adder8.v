module ripple_carry_adder8(
  input [7:0] A,
  input [7:0] B,
  input Cin,
  output [7:0] S,
  output Cout
);
  wire c1, c2, c3, c4, c5, c6, c7;

  full_adder FA0(A[0], B[0], Cin, S[0], c1);
  full_adder FA1(A[1], B[1], c1,  S[1], c2);
  full_adder FA2(A[2], B[2], c2,  S[2], c3);
  full_adder FA3(A[3], B[3], c3,  S[3], c4);
  full_adder FA4(A[4], B[4], c4,  S[4], c5);
  full_adder FA5(A[5], B[5], c5,  S[5], c6);
  full_adder FA6(A[6], B[6], c6,  S[6], c7);
  full_adder FA7(A[7], B[7], c7,  S[7], Cout);
endmodule
