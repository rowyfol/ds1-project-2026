module tb_full_adder;
  reg A, B, Cin;
  wire S, Co;
  full_adder DUT(
    .A(A),
    .B(B),
    .Cin(Cin),
    .S(S),
  .Co(Co)
  );
  initial begin
    A=0; B=0; Cin=0;
    #20;

    A=0; B=1; Cin=1;
    #20;

    A=1; B=1; Cin=1;
    #20;

    $stop;
  end
endmodule
