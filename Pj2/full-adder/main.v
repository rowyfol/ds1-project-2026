module full_adder(
  input A,
  input B,
  input Cin,
  output S,
  output Co
);
  parameter t_sum = 10;
  parameter t_co  = 8;
  assign #(t_sum) S = A ^ B ^ Cin;
  assign #(t_co)  Co = (A&B) | (A&Cin) | (B&Cin);
endmodule
