#!/usr/bin/env python

import fileinput
import numpy

numbers = []

for line in fileinput.input():
    if ',' in line:
        try:
            for num in line.split(','):
                numbers.append(float(num))
        except:
            continue
        
print '%0.2f' % numpy.average(numbers)
