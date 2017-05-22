// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

	// Place the address of first register of screen in Memory[17]
	@16384
	D=A
	@17
	M=D

(LISTENER)
	// No key press
	@KBD
	D=M
	@CLEAR
	D;JEQ

	// Key press
	@KBD
	D=M
	@BLACK
	D;JGT

(BLACK)  // Creation of black 
	// Check to make sure the screen isn't completely full, and if it is, then go back to listener
	@17
	D=M
	@24576
	D=A-D
	@LISTENER
	D;JEQ
	// Turn screen black at current address
	@17
	A=M
	M=-1
	// Increment address
	@17
	D=M
	@1
	D=D+A
	@17
	M=D
	@LISTENER
	0;JMP

(CLEAR)
	// Check to make sure the screen isn't already white, and if it is, go back to listener
	@17
	D=M
	@16383
	D=D-A
	@LISTENER
	D;JEQ
	// Turn screen white at current address
	@17
	A=M
	M=0
	@17
	D=M
	@1
	D=D-A
	@17
	M=D
	@LISTENER
	0;JMP


	

