module full_adder(
  input A,
  input B,
  input Cin,
  output S,
  output Co
);
  parameter t_sum = 12;
  parameter t_co  = 7;
  assign #(t_sum) S = A ^ B ^ Cin;
  assign #(t_co)  Co = (A&B) | (A&Cin) | (B&Cin);
endmodule
