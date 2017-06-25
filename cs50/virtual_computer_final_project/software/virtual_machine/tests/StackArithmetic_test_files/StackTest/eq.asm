// push constant 17
@17 // arg2
D=A // store arg2 in D
@SP // A=0
A=M // A=256
M=D // set current stack register to D=17
@SP // Go back to stack pointer
M=M+1  // Increment stack pointer

// push constant 17
@17 // arg2
D=A // store arg2 in D
@SP // A=0
A=M // A=257 (because we incremented it)
M=D // set current stack register RAM[257]=D
@SP // go back to stack pointer
M=M+1 // increment stack pointer

// Add
@SP // A=0
A=M-1 // A=257
D=M // D=Memory[257]=17
@SP
A=M-1 // A=256
D=D-M // D=17-Memory[256], so D=0
@FALSE
D;JNE
@2
D=A
@SP  // A=0
M=M-D
A=M  // A = 256
M=-1
@END
0;JMP
(FALSE)
@2
D=A
@SP // A=0
M=M-D  // M=258-2
A=M // A=256
M=0
(END)
@2
D=A
@SP
A=M+D
