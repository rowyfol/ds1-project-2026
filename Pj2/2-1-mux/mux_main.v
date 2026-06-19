module mux_main(
  input I0,
  input I1,
  input Sel,
  output Y
);
  parameter t_mux = 5;
  assign #(t_mux) Y = Sel ? I1 : I0;
endmodule
