#!/usr/bin/zsh


cp challenge2.jpg /tmp/
cd /tmp/

steghide extract \
    -sf challenge1.jpg \
    -p "spoon"

cat steganography.txt | less
