#!/usr/bin/env python

from sys import argv
import re

asmfile = argv[1]

def commandType(line):
    aregex = r'^\s*[\@]{1}([a-zA-Z\_\:\$\.]*[\d]*)'
    cregex = r'^[\s]*(([AMD]{0,3})[\=]{1})?(([AMD\d\+\!\-\&\|]{1,3})[\;]{1})?(([JEGQLTPNM]{0,3}))?'
    lregex = r'^\s*\({1}([a-zA-Z\_0-9\:\$\.]+)\){1}'
    if(re.match(r'^\s*/{2}|(\r?\n)',line)):
        return "COMMENT"
    elif(re.match(aregex, line)):
        return "A_COMMAND"
    elif(re.match(lregex, line)):
        return "L_COMMAND"
    elif(re.match(cregex, line)):
        return "C_COMMAND"
    else:
        return "Invalid syntax"

def loadSymbols(asmfile):
    symbolTable={"SP":"0", "LCL":"1", "ARG":"2", "THIS":"3", "THAT":"4", "SCREEN":"16384", "KBD":"24576",
                 "R0":"0", "R1":"1", "R2":"2", "R3":"3", "R4":"4", "R5":"5", "R6":"6", "R7":"7", "R8":"8",
                 "R9":"9", "R10":"10", "R11":"11", "R12":"12", "R13":"13", "R14":"14", "R15":"15"}
    currentCommand = 0
    currentRAM = 16
    with open(asmfile, "r") as infile:
        for line in infile:
            if(commandType(line)=="COMMENT"):
                pass
            elif(commandType(line)=="A_COMMAND"):
                currentCommand += 1
            elif(commandType(line)=="L_COMMAND"):
                newsymbol = re.match(r'^\s*\({1}([a-zA-Z\_0-9\:\$\.]+)\){1}',line).group(1)
                symbolTable.update({newsymbol:currentCommand})
            elif(commandType(line)=="C_COMMAND"):
                currentCommand += 1
            else:
                pass

    with open(asmfile,"r") as infiletwo:
        for line in infiletwo:
            if(commandType(line)=="A_COMMAND"):
                if(re.match(r'^\s*[\@]{1}([a-zA-Z\_\:\$\.]+[\d]*)', line)):
                    symbol = re.match(r'^\s*[\@]{1}([a-zA-Z\_\:\$\.]+[\d]*)', line).group(1)
                    if(symbolTable.get(symbol)):
                        pass
                    else:
                        symbolTable.update({symbol:currentRAM})
                        currentRAM += 1
            else:
                pass
    return symbolTable

symbolTable2 = loadSymbols(asmfile)

def symbol(line):
    global symbolTable2
    aregex = r'^\s*[\@]{1}([a-zA-Z\_\:\$\.]*[\d]*)'
    if(commandType(line)=="A_COMMAND"):
        if(re.match(r'^\s*[\@]{1}([0-9]+)',line)):
            # If the command is a integer address, convert integer to binary
            #print(re.match(r'^\s*[\@]{1}([0-9]+)', line).group(1))
            binaryAddress = "{0:015b}".format(int(re.match(r'^\s*[\@]{1}([0-9]+)', line).group(1)))
            sBinaryAddress = "0" + str(binaryAddress)
            return sBinaryAddress
        elif(re.match(r'^\s*[\@]{1}([a-zA-Z\_\:\$\.]*[\d]*)', line)):
            aw = re.match(aregex, line).group(1)
            lookup = symbolTable2[aw]
            ba = "{0:015b}".format(int(lookup))
            sba = "0" + str(ba)
            return sba
        else:
            pass
    elif(commandType(line)=="L_COMMAND"):
        return (re.match(r'^\s*\({1}([a-zA-Z\_0-9\:\$\.]+)\){1}', line).group(1))

def dest(line):
    cregex = r'^[\s]*(([AMD]{0,3})[\=]{1})?(([AMD\d\+\!\-\&\|]{1,3})[\;]?)?(([JEGQLTPNM]{0,3}))?'
    if(commandType(line)=="C_COMMAND"):
        return (re.search(cregex, line).group(2))

def comp(line):
    cregex = r'^[\s]*(([AMD]{0,3})[\=]{1})?(([AMD\d\+\!\-\&\|]{1,3})[\;]?)?(([JEGQLTPNM]{0,3}))?'
    if(commandType(line)=="C_COMMAND"):
        return re.search(cregex, line).group(4)

def jump(line):
    cregex = r'^[\s]*(([AMD]{0,3})[\=]{1})?(([AMD\d\+\!\-\&\|]{1,3})[\;]?)?(([JEGQLTPNM]{0,3}))?'
    if(commandType(line)=="C_COMMAND"):
        return (re.search(cregex, line).group(6))
