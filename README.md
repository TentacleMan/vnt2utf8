# vnt2utf8.py version 0.9

Python script to convert between base64-encoded Vnote files exported
from the Memo app that came with my Android phone and UTF8 text. Not
rigorously tested. Written by an inexperienced coder, may explode or
kill kittens. Writes output to stdout or optionally to file. No
special care is taken to ensure that converted text actually is UTF8.

BSD-style license included inside the script.

Copyright (c) 2015 TentacleMan

---------

CHANGELOG

Version 0.9 - actually the second release. Discovered argparse, output
can now be saved to file by a supplied script argument.