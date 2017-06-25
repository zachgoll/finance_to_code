#!/usr/bin/env python

import sys
import os
import re
from parser import Parser


class CodeWriter(object):

    counter1 = 0
    counter2 = 0
    counter3 = 0
    funcounter = 0
    filenum = 0
    static = 0

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for writing.'''
        self.outfile = open(self.filename, "w")
        return self.outfile


    def setFileName(self, filename):
        '''Inform CodeWriter that a new file has been opened and is ready'''
        CodeWriter.filenum += 1
        CodeWriter.static += 16
        return Parser(filename)

    def extractFile(self, parsefile):
        afile = open(parsefile, "r")
        contentString = ""
        for line in afile:
            contentString += line
        afile.close()
        return contentString

    def writeArithmetic(self, outfile, command):
        '''Convert the given arithmetic command into assembly code'''
        command = command.lower()

        if command == "add":
            outfile.write(self.extractFile("asm_functions/add.asm"))
        elif command =="sub":
            outfile.write(self.extractFile("asm_functions/sub.asm"))
        elif command =="neg":
            outfile.write(self.extractFile("asm_functions/neg.asm"))
        elif command =="eq":
            asmcommand1 = self.extractFile("asm_functions/eq.asm")

            n1 = asmcommand1.replace("TRUE_ONE", "TRUE_ONE" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            n2 = n1.replace("END_ONE", "END_ONE" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            outfile.write(n2)

        elif command =="gt":
            asmcommand1 = self.extractFile("asm_functions/gt.asm")

            n1 = asmcommand1.replace("TRUE_TWO", "TRUE_TWO" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            n2 = n1.replace("END_TWO", "END_TWO" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            outfile.write(n2)

        elif command =="lt":
            asmcommand1 = self.extractFile("asm_functions/lt.asm")

            n1 = asmcommand1.replace("TRUE_THREE", "TRUE_THREE" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            n2 = n1.replace("END_THREE", "END_THREE" + str(CodeWriter.counter1))
            CodeWriter.counter1 += 1

            outfile.write(n2)

        elif command =="and":
            outfile.write(self.extractFile("asm_functions/and.asm"))
        elif command =="or":
            outfile.write(self.extractFile("asm_functions/or.asm"))
        elif command =="not":
            outfile.write(self.extractFile("asm_functions/not.asm"))

    def writePushPop(self, outfile, command, segment, index):
        '''Convert the given push/pop command into assembly code'''

        firstLine = "@" + index + "\n"

        if command == "C_PUSH":
            if segment == "argument":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_arg.asm"))

            elif segment == "local":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_local.asm"))

            elif segment == "static":

                fileindex = int(index) + CodeWriter.static

                outfile.write("@" + str(fileindex) + "\n")
                outfile.write(self.extractFile("asm_functions/push_static.asm"))

            elif segment == "constant":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_constant.asm"))

            elif segment == "this":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_this.asm"))

            elif segment == "that":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_that.asm"))

            elif segment == "pointer":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_pointer.asm"))

            elif segment == "temp":

                outfile.write(firstLine)
                outfile.write(self.extractFile("asm_functions/push_temp.asm"))

        elif command == "C_POP":
            if segment == "argument":

                argu1 = self.extractFile("asm_functions/pop_arg.asm")
                argu2 = argu1.replace("variable", index)
                outfile.write(argu2)

            elif segment == "local":

                loc1 = self.extractFile("asm_functions/pop_local.asm")
                loc2 = loc1.replace("variable", index)
                outfile.write(loc2)

            elif segment == "static":

                fileindex = int(index) + CodeWriter.static

                outfile.write(self.extractFile("asm_functions/pop_static.asm"))
                outfile.write("@" + str(fileindex) + "\nM=D\n")

            elif segment == "constant":

                pass

            elif segment == "this":

                this1 = self.extractFile("asm_functions/pop_this.asm")
                this2 = this1.replace("variable", index)
                outfile.write(this2)

            elif segment == "that":

                that1 = self.extractFile("asm_functions/pop_that.asm")
                that2 = that1.replace("variable", index)
                outfile.write(that2)

            elif segment == "pointer":

                point1 = self.extractFile("asm_functions/pop_pointer.asm")
                point2 = point1.replace('variable', index)
                outfile.write(point2)

            elif segment == "temp":

                temp1 = self.extractFile("asm_functions/pop_temp.asm")
                temp2 = temp1.replace('variable', index)
                outfile.write(temp2)

    def writeInit(self, outfile):
        '''Writes assembly code that effects the VM initialization (beginning of output file)'''

        outfile.write('@256\n'+'D=A\n'+'@SP\n'+'M=D\n')
        self.writeCall(outfile, "Sys.init", "0")

    def writeLabel(self, outfile, label):
        '''Sets a given label to an address in memory'''
        outfile.write('(' + label + ')\n')

    def writeGoto(self, outfile, label):
        '''Go to the program instruction address of the given label'''
        outfile.write('@' + label + '\n0;JMP\n')

    def writeIf(self, outfile, label):
        '''Under a certain condition, current state of program changes and goes to label'''

        popstack = self.extractFile("asm_functions/pop_temp.asm")
        popstack2 = popstack.replace('variable', '0')

        outfile.write(popstack2 + '@R5\nD=M\n@' + label + '\nD;JNE\n')

    def writeCall(self, outfile, functionName, numArgs):
        '''Calls a function'''

        retAddress = '@RETURN.'+ functionName + '.' + str(CodeWriter.funcounter)

        outfile.write(retAddress + '\n')
        functionCall = self.extractFile("asm_functions/function_call.asm")
        functionCall2 = functionCall.replace("numARGS", str(numArgs))

        outfile.write(functionCall2)

        ret = retAddress.replace("@","")

        self.writeGoto(outfile,functionName)
        self.writeLabel(outfile, ret)

        CodeWriter.funcounter += 1

    def writeReturn(self, outfile):
        '''Returns the result of a function to the top of the stack and erases args'''

        outfile.write(self.extractFile("asm_functions/function_ret.asm"))

    def writeFunction(self, outfile, functionName, numLocals):
        '''Initializes a function for use'''

        num = int(numLocals)

        self.writeLabel(outfile, functionName)

        while num > 0:
            outfile.write('@0\n')
            outfile.write(self.extractFile("asm_functions/push_constant.asm"))
            num -= 1
