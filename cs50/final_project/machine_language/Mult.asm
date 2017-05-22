// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	//  Initialize values at addresses used in calculation
	@R2
	M=0
	@R3
	M=0

	//  Beginning of Loop
(LOOP)

	// 	Check to make sure the R3 is not >= R0
	//  This ensures that the loop runs an equal amount of times to the value of the first operand R0
	//  If it is, exit loop and end program
	@R3
	D=M
	@R0
	D=D-M
	@END
	D;JGE

	//  Increment R2 by the value of the second operand R1
	@R1
	D=M
	@R2
	M=M+D

	//  Increment the counter by 1
	@R3
	M=M+1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP