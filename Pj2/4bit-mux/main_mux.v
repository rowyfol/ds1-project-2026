module mux4bit(
input [3:0] A,
input [3:0] B,
input Sel,
output [3:0] Y
);
mux2_to_1 M0(A[0],B[0],Sel,Y[0]);
mux2_to_1 M1(A[1],B[1],Sel,Y[1]);
mux2_to_1 M2(A[2],B[2],Sel,Y[2]);
mux2_to_1 M3(A[3],B[3],Sel,Y[3]);
endmodule
