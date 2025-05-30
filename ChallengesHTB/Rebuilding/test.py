#!/usr/bin/python3


import time
import sys


data = ''
for local_10 in range(0, 32):
    for local_c in range(0, 6):
        if local_c  == local_10 % 6:
            data += "."
        else:
            data += " "
    sys.stdout.write('\r' + data)
    sys.stdout.flush()
    time.sleep(0.1)


print()



