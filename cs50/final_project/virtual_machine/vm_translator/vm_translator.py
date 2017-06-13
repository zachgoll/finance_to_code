#!/usr/bin/env python
"""assembler.py, by Zach Gollwitzer, 2017-05-23
This program is part of the Nand2Tetris project, and is
the first portion of the Virtual Machine which will convert an intermediate
language into Hack Machine language.
"""
import sys
import os
import re
from parser import Parser
from code_writer import CodeWriter

def main():
    '''Main entry point for the script.'''

    # For each .vm file, create a parser object
    filetrue = os.path.isfile(sys.argv[1])
    dirtrue = os.path.isdir(sys.argv[1])
    vmfiles = []

    # Rename directory as a ".asm" file for later use
    finame = os.path.basename(os.path.normpath(sys.argv[1])) + ".asm"

    # Get file path with .asm file appended
    dirname = os.path.join(sys.argv[1], finame)

    # Create list of files to convert and add to asm file
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
        print "usage: 'python <file.vm> or <dirname/>'"

    out = cw.constructor()
    cw.writeInit(out)

    with out as outfile:

        for files in vmfiles:

            # Create new instance of class Parser()
            p = cw.setFileName(files)

            with p.constructor() as infile:

                    for line in infile:

                        if p.commandType(line)=="comments":

                            pass

                        elif p.commandType(line)=="C_ARITHMETIC":

                            cw.writeArithmetic(outfile, p.args(line)[0])


                        elif p.commandType(line)=="C_IF":

                            # Handle if-goto command
                            cw.writeIf(outfile, p.args(line)[1])

                        elif p.commandType(line)=="C_GOTO":

                            # Handle goto command
                            cw.writeGoto(outfile, p.args(line)[1])

                        elif p.commandType(line)=="C_RETURN":

                            # Return function result
                            cw.writeReturn(outfile)


                        elif p.commandType(line)=="C_LABEL":

                            # Set label address
                            cw.writeLabel(outfile, p.args(line)[1])


                        elif p.commandType(line)=="C_CALL":

                            # Handle function calls
                            cw.writeCall(outfile, p.args(line)[1], p.args(line)[2])

                        elif p.commandType(line)=="C_FUNCTION":

                            cw.writeFunction(outfile, p.args(line)[1], p.args(line)[2])

                        elif p.commandType(line)=="C_PUSH" or "C_POP":

                            cw.writePushPop(outfile, p.commandType(line), p.args(line)[1], p.args(line)[2])


# __name__ variable is automatically set to "__main__" for the source file
# which is called by the Python compiler.
if __name__ == "__main__":
	sys.exit(main())
