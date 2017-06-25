// Frame = LCL
@LCL
D=M
@R13
M=D

// RET = *(FRAME-5)
@5
D=A
@R13
A=M-D
D=M
@R14
M=D

// *ARG = pop()
@0
D=A
@ARG
M=M+D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
M=M-D
@SP
M=M-1

// SP = ARG+1
@ARG
D=M
@SP
M=D+1

// THAT = *(FRAME-1)
@1
D=A
@R13
A=M-D
D=M
@THAT
M=D

// THIS = *(FRAME-2)
@2
D=A
@R13
A=M-D
D=M
@THIS
M=D

// ARG = *(FRAME-3)
@3
D=A
@R13
A=M-D
D=M
@ARG
M=D

// LCL = *(FRAME-4)
@4
D=A
@R13
A=M-D
D=M
@LCL
M=D

// goto ret
@R5
0;JMP
