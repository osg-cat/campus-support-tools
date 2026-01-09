#!/usr/bin/env python3

import getpass
import os
import platform
import socket
import sys
import time

arguments = None
if len(sys.argv) > 1:
    arguments = '"' + ' '.join(sys.argv[1:]) + '"'

uname = platform.uname()

# print(__doc__, file=sys.stderr)
print(f'Time      : {time.strftime("%Y-%m-%d (%a) %H:%M:%S %Z")}')
print(f'User@Host : {getpass.getuser()}@{socket.gethostname()}')
print(f'System    : {uname[0]} {uname[2]} {uname[4]}')
print(f'Python    : {platform.python_version()}')
print(f'Program   : {sys.executable}')
print(f'Script    : {os.path.abspath(__file__)}')
print(f'Args      : {arguments}')
