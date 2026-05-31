`timescale 1ns/1ps

module test;

    // Testbench variables
    reg a, b, c;
    wire h, g;

    // Instantiate the main module
    main uut(
        .a(a),
        .b(b),
        .c(c),
        .h(h),
        .g(g)
    );

    initial begin
        // Setup waveform generation
        $dumpfile("wave.vcd");
        $dumpvars(0, test);

        // Monitor changes on inputs and outputs
        $monitor("Time=%0t | a=%b b=%b c=%b | g=%b h=%b", $time, a, b, c, g, h);

        // --- Test Cases ---
        
        // Initial state
        a = 0; b = 0; c = 0;
        #20; 

        // Test case 2
        a = 1; b = 0; c = 1;
        #20; 

        // Test case 3
        a = 1; b = 1; c = 1;
        #20; 

        // End the simulation
        $finish;
    end

endmodule
