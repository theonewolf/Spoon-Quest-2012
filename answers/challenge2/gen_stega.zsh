#!/usr/bin/zsh

steghide embed \
    -cf steganography.jpg \
    -ef steganography.txt \
    -sf challenge2.jpg \
    -p "spoon"
