#!/usr/bin/env python

import fileinput
import sys

key = open('key.txt','rb')
cipher = open('ciphertext.txt','rb')

cipher = cipher.read()
cipher = cipher.replace('\n', ' ')
key = bytearray(key.read())


for i,b in enumerate(cipher.split(' ')):
    if b != '':
        sys.stdout.write('%c' % (int(b,16) ^ key[i]))
