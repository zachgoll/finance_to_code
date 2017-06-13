#!/usr/bin/env python

import sys
import os
import re


class Parser(object):

    def __init__(self, filename):

        self.filename = filename

    def constructor(self):
        '''Open the file for parsing'''
        self.infile = open(self.filename, "r")
        return self.infile

    def commandType(self, line):
        '''Reads the line and returns the command type'''
        self.ll = line.lower()

        if re.match(r'^\s*/{2}|(\r?\n)', line):
            return "comments"
        elif re.match(r'^\s*if-goto{1}', line):
            return "C_IF"
        elif re.match(r'^\s*add|neg|sub|eq|gt|lt|and|or|not{1}', line):
            return "C_ARITHMETIC"
        elif re.match(r'^\s*push{1}', line):
            return "C_PUSH"
        elif re.match(r'^\s*pop{1}', line):
            return "C_POP"
        elif re.match(r'^\s*label{1}', line):
            return "C_LABEL"
        elif re.match(r'^\s*goto{1}', line):
            return "C_GOTO"
        elif re.match(r'^\s*function{1}', line):
            return "C_FUNCTION"
        elif re.match(r'^\s*return{1}', line):
            return "C_RETURN"
        elif re.match(r'^\s*call{1}', line):
            return "C_CALL"

    def parse(self, line):

        regex = r'[\s]*([a-zA-Z\-]+){1}[\s]{1}([a-zA-Z0-9\_\.\:]+)?[\s]?([\d]+)?'

        if self.commandType(line) == "comments":
            pass
        else:
            com = re.match(regex, line).group(1)
            mid = re.match(regex, line).group(2)
            dig = re.match(regex, line).group(3)

            if mid == None:
                return [com]
            elif dig == None:
                return [com, mid]
            else:
                return [com, mid, dig]

    def args(self, line):
        '''Reads the line and returns the first argument if there is one'''

        a = self.parse(line)
        return a
