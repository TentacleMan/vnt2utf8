# vnt2utf8.py version 1.0

Python script to convert between base64-encoded Vnote files exported
from the Memo app that came with my Android phone and UTF8 text. Not
rigorously tested. Written by an inexperienced coder, may explode or
kill kittens. Writes output to stdout or optionally to file. No
special care is taken to ensure that converted text actually is UTF8.

BSD-style license included inside the script.

Copyright (c) 2016 El Topo (TentacleMan)

---------

CHANGELOG

Version 1.0 - wrapping of long lines is now supported.

Version 0.9 - actually the second release. Discovered argparse, output
can now be saved to file by a supplied script argument.
