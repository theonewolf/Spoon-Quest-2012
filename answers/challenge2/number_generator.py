#!/usr/bin/env python

import numpy
import random

numbers = [random.gauss(3.1415926, 3) for i in xrange(10000)]

while (numpy.mean(numbers) - 3.1415926 > 0.000001):
    numbers = [random.gauss(3.1415926, 3) for i in xrange(10000)]

for i,num in enumerate(numbers):
    if (i+1) % 7 == 0 or i == len(numbers) - 1:
        print '%f' % num
    else:
        print '%f,' % num,
