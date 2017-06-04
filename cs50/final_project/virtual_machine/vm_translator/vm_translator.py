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

    # Create list of files to convert to .asm
    if dirtrue:
        fi = os.listdir(sys.argv[1])
        for names in fi:
            if names.endswith(".vm"):
                vmfiles.append(sys.argv[1]+names)
    elif filetrue:
        di = sys.argv[1]
        if di.endswith(".vm"):
            vmfiles.append(di)
        else:
            print "invalid filetype: only input .vm files"
    else:
        print "usage: 'python <file.vm/dir>'"

    cw = CodeWriter("outfile.asm")

    for files in vmfiles:

        p = Parser(files)

        with p.constructor() as infile:
            for line in infile:
                commandType = p.commandType(line)
                print commandType










class CodeWriter(object):

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for writing.'''
        return "hello, this is the Codewriter constructor speaking"


    def setFileName(self, filename):
        '''Inform CodeWriter that a new file has been opened and is ready'''

        pass

    def writeArithmetic(self, command):
        '''Convert the given arithmetic command into assembly code'''

        pass

    def writePushPop(self, command, segement, index):
        '''Convert the given push/pop command into assembly code'''

        pass

    def close(self):
        '''Close the file'''

        pass

class Parser(object):

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for parsing'''
        self.infile = open(self.filename, "r")
        return self.infile


    def commandType(self, line):
        '''Reads the line and returns the command type'''
        arithmeticList  = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']

        if re.match(r'^\s*/{2}|(\r?\n)', line):
            return "comments"
        elif any(word in line.lower() for word in arithmeticList):
            return "C_ARITHMETIC"
        """elif re.match(push, line):
            return "C_PUSH"
        elif re.match(pop, line):
            return "C_POP"
        elif re.match(label, line):
            return "C_LABEL"
        elif re.match(goto, line):
            return "C_GOTO"
        elif re.match(ifs, line):
            return "C_IF"
        elif re.match(func, line):
            return "C_FUNCTION"
        elif re.match(ret, line):
            return "C_RETURN"
        elif re.match(call, line):
            return "C_CALL"
            """

    def arg1(self, line):
        '''Reads the line and returns the first argument if there is one'''
        pass

    def arg2(self, line):
        '''Reads the line and returns the second argument if there is one'''
        pass




# If the name of the module is "__main__", then run the main function, else,
# do not automatically run main() because it is an imported module.
# __name__ variable is automatically set to "__main__" for the source file
# which is called by the Python compiler.
if __name__ == "__main__":
	sys.exit(main())
