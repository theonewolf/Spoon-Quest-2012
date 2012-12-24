#!/usr/bin/env python

import fileinput

plain = open('plaintext.txt','rb')
key = open('key.txt','rb')
cipher = open('ciphertext.txt','wb')

plain = bytearray(plain.read())
key = bytearray(key.read())

for i,b in enumerate(plain):
    if (i + 1) % 16 == 0:
        cipher.write('0x%0.2x\n' % (b ^ key[i]))
    else:
        cipher.write('0x%0.2x ' % (b ^ key[i]))
