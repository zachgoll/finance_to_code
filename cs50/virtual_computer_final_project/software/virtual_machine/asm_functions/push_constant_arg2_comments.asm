// push constant 17
// @17 // This is commented out because the CodeWriter is going to have to insert "@arg2" at the beginning of this program
D=A // store arg2 in D
@SP // A=0
A=M // A=256
M=D // set current stack register to D=17
@SP // Go back to stack pointer
M=M+1  // Increment stack pointer
