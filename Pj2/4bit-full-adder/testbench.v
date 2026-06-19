module tb_adder4;
  reg [3:0] A, B;
  reg Cin;
  wire [3:0] S;
  wire Cout;
  adder4 DUT(
      A, B, Cin, S, Cout
  );
  initial begin

  A=4'b0011;
  B=4'b0101;
  Cin=0;
  #50;

  A=4'b1111;
  B=4'b0001;
  Cin=0;
  #50;

  A=4'b1010;
  B=4'b0110;
  Cin=1;
  #50;

  $stop;
  end
endmodule
