@256
D=A
@SP
M=D
@RETURN.Sys.init.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
@0
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@Sys.init
0;JMP
(RETURN.Sys.init.0)
(Sys.init)
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@RETURN.Sys.main.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
@0
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@Sys.main
0;JMP
(RETURN.Sys.main.1)
@1
D=A
@R5
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
(LOOP)
@LOOP
0;JMP
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
M=M+D
@SP
A=M-1
D=M
@LCL
A=M
M=D
@1
D=A
@LCL
M=M-D
@SP
M=M-1
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
M=M+D
@SP
A=M-1
D=M
@LCL
A=M
M=D
@2
D=A
@LCL
M=M-D
@SP
M=M-1
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
M=M+D
@SP
A=M-1
D=M
@LCL
A=M
M=D
@3
D=A
@LCL
M=M-D
@SP
M=M-1
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
@RETURN.Sys.add12.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@LCL
M=D
@1
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@Sys.add12
0;JMP
(RETURN.Sys.add12.2)
@0
D=A
@R5
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@0
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@3
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@4
D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@LCL
D=M
@R13
M=D
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
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
@ARG
D=M
@SP
M=D+1
@1
D=A
@R13
A=M-D
D=M
@THAT
M=D
@2
D=A
@R13
A=M-D
D=M
@THIS
M=D
@3
D=A
@R13
A=M-D
D=M
@ARG
M=D
@4
D=A
@R13
A=M-D
D=M
@LCL
M=D
@R14
A=M
0;JMP
(Sys.add12)
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@THIS
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1
@LCL
D=M
@R13
M=D
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
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
@ARG
D=M
@SP
M=D+1
@1
D=A
@R13
A=M-D
D=M
@THAT
M=D
@2
D=A
@R13
A=M-D
D=M
@THIS
M=D
@3
D=A
@R13
A=M-D
D=M
@ARG
M=D
@4
D=A
@R13
A=M-D
D=M
@LCL
M=D
@R14
A=M
0;JMP