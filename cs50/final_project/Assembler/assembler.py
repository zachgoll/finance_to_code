#!/usr/bin/env python
"""assembler.py, by Zach Gollwitzer, 2017-05-23
This program is part of the Nand2Tetris project, and is
the assembler that will convert the Hack Computer machine code
to binary code to be run on the hardware built in chapter's 1, 2, 3, and 5
"""
import parser
import code
import re
from sys import argv
#import symbol_table

asmfile = argv[1]
hackfile = argv[1].replace("asm", "hack")

def main():
	with open(asmfile, "r") as infile:
		with open(hackfile, "w") as outfile:
			for line in infile:
				if(re.match(r'^\s*/{2}|(\r?\n)',line)):
					pass
				else:
					if(parser.commandType(line)=="A_COMMAND"):
						commandA = parser.symbol(line)
						outfile.write(commandA+"\n")
					elif(parser.commandType(line)=="L_COMMAND"):
						pass
					elif(parser.commandType(line)=="C_COMMAND"):
						commandC = code.command(line)
						outfile.write(commandC+"\n")
					else:
						print("invalid syntax")

# If the name of the module is "__main__", then run the main function, else,
# do not automatically run main() because it is an imported module.
# __name__ variable is automatically set to "__main__" for the source file
# which is called by the Python compiler.
if __name__ == "__main__":
	main()
