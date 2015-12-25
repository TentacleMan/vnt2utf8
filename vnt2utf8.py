#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script to convert between base64-encoded Vnote files exported from
# the Memo app that came with my Android phone and UTF8 text. Not
# rigorously tested. Written by a newb coder, may explode or kill
# kittens. Dumps output on stdout and forgets it ever happened. No
# special care is taken to ensure that converted text actually is
# UTF8.

# Copyright (c) 2015 TentacleMan

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import quopri

usage = 'Usage: vnt2utf8.py FILE'
magicword = 'BODY;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'

#
# base64 decoding workhorse function
#
def decode_vnote(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.translate(None, '\r\n')
            if line.startswith(magicword):
                line = line[45:]
                line = quopri.decodestring(line)
                print line
                break

# --- Main program ---    
if len(sys.argv) > 1:
# infile present, or missing and options given
    if len(sys.argv) == 2:
        if sys.argv[1][0] == '-': # argv[1] is an option such as '-h'
            print usage
            exit(0)
    # open file and decode it, print to stdout
    decode_vnote(sys.argv[1])
# just the script name present on the command line
else:
    print usage
