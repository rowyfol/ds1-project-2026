module tb_main_mux;

reg [3:0] A, B;
reg Sel;

wire [3:0] Y;
mux4bit DUT(
    A,B,Sel,Y
);

initial begin

A=4'b1010;
B=4'b0101;
Sel=0;
#30;

Sel=1;
#30;

A=4'b1111;
B=4'b0000;
Sel=0;
#30;

$stop;

end
endmodule
