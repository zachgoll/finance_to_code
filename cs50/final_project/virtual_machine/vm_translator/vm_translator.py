#!/usr/bin/env python
"""assembler.py, by Zach Gollwitzer, 2017-05-23
This program is part of the Nand2Tetris project, and is
the first portion of the Virtual Machine which will convert an intermediate
language into Hack Machine language.
"""
import sys
import os
import re

def main():
    '''Main entry point for the script.'''

    # For each .vm file, create a parser object
    filetrue = os.path.isfile(sys.argv[1])
    dirtrue = os.path.isdir(sys.argv[1])
    vmfiles = []
    dirname = os.path.basename(os.path.normpath(sys.argv[1])) + ".asm"

    # Create list of files to convert to .asm
    if dirtrue:
        cw = CodeWriter(dirname)
        fi = os.listdir(sys.argv[1])
        for names in fi:
            if names.endswith(".vm"):
                vmfiles.append(sys.argv[1]+names)

    elif filetrue:
        di = sys.argv[1]
        if di.endswith(".vm"):
            vmfiles.append(di)
            tr = vmfiles[0]
            trs = tr.replace("vm", "asm")
            cw = CodeWriter(trs)
        else:
            print "invalid filetype: only input .vm files"
    else:
        print "usage: 'python <file.vm/dir>'"


    out = cw.constructor()
    print vmfiles
    with out as outfile:
        print outfile
        for files in vmfiles:
            print "WE HAVE STARTED A NEW FILE"
            # Create new instance of class Parser()
            p = cw.setFileName(files)

            with p.constructor() as infile:
                    for line in infile:
                        # If line format is command arg1 arg2
                        if p.arg2(line):
                            if p.commandType(line)=="C_PUSH" or "C_POP":
                                print line
                                cw.writePushPop(outfile, p.commandType(line), p.arg1(line), p.arg2(line))
                        # If line format is command or command arg1
                        elif p.arg1(line):
                            if p.commandType(line)=="C_ARITHMETIC":
                                print line
                                cw.writeArithmetic(outfile, p.arg1(line))


class CodeWriter(object):

    counter1 = 0
    counter2 = 0
    counter3 = 0

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for writing.'''
        self.outfile = open(self.filename, "w")
        return self.outfile


    def setFileName(self, filename):
        '''Inform CodeWriter that a new file has been opened and is ready'''
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

                outfile.write(firstLine)
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

                stat1 = self.extractFile("asm_functions/pop_static.asm")
                stat2 = stat1.replace("variable", index)
                outfile.write(stat2)

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

class Parser(object):

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for parsing'''
        self.infile = open(self.filename, "r")
        return self.infile

    def commandType(self, line):
        '''Reads the line and returns the command type'''
        self.arithmeticList  = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        self.ll = line.lower()

        if re.match(r'^\s*/{2}|(\r?\n)', line):
            return "comments"
        elif 'if' in self.ll:
            return "C_IF"
        elif any(word in self.ll for word in self.arithmeticList):
            return "C_ARITHMETIC"
        elif 'push' in self.ll:
            return "C_PUSH"
        elif 'pop' in self.ll:
            return "C_POP"
        elif 'label' in self.ll:
            return "C_LABEL"
        elif 'goto' in self.ll:
            return "C_GOTO"
        elif 'function' in self.ll:
            return "C_FUNCTION"
        elif 'return' in self.ll:
            return "C_RETURN"
        elif 'call' in self.ll:
            return "C_CALL"


    def arg1(self, line):
        '''Reads the line and returns the first argument if there is one'''
        self.arg1List = ['argument', 'local', 'static', 'constant', 'this', 'that',
                     'pointer', 'temp']
        self.commandList = ['push', 'pop', 'label', 'goto', 'if-goto','function','call']
        self.ll = line.lower()
        arg1 = []

        if re.match(r'^\s*/{2}|(\r?\n)', line):
            pass
        elif self.commandType(line) == "C_RETURN":
            pass
        else:
            for y in self.arg1List:
                if y in line:
                    return y
            for x in self.arithmeticList:
                if x in line:
                    return x

        return arg1

    def arg2(self, line):
        '''Reads the line and returns the second argument if there is one'''
        if re.match(r'^\s*/{2}|(\r?\n)', line):
            pass
        elif re.search(r'[\d]+', line):
            return re.search(r'([\d]+)', line).group(1)




# If the name of the module is "__main__", then run the main function, else,
# do not automatically run main() because it is an imported module.
# __name__ variable is automatically set to "__main__" for the source file
# which is called by the Python compiler.
if __name__ == "__main__":
	sys.exit(main())
