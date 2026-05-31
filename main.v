`timescale 1ns/1ps

module main(
    input a,
    input b,
    input c,
    output h,
    output g
);

    // Internal wires connecting the gates
    wire w1, w2, w3;

    // Gate level description with delays
    not  #(2) g1 (w1, a);
    and  #(5) g2 (w2, a, b);
    or   #(5) g3 (w3, w1, w2, b);
    
    nand #(4) g4 (g, c, b);
    nor  #(4) g5 (h, w3, g);

endmodule
