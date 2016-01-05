#!/usr/bin/python2
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
import argparse
import quopri

# usage = 'Usage: vnt2utf8.py FILE'
magicword = 'BODY;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'

#
# base64 decoding workhorse function
#
def decode_vnote(infile, outfile):
    for line in infile:
        line = line.translate(None, '\r\n')
        if line.startswith(magicword):
            line = line[45:]
            line = quopri.decodestring(line)
            outfile.write(line)
            break

# --- Main program ---    

parser = argparse.ArgumentParser(description='Convert Vnote base64 to UTF-8 text.')
parser.add_argument('INFILE', help='Vnote file to convert.', type=argparse.FileType('r'))
parser.add_argument('-o', '--outfile', dest='OUTFILE', help='File to write to (default: stdout)', type=argparse.FileType('w'), default='-')
args = parser.parse_args()

decode_vnote(args.INFILE, args.OUTFILE)

