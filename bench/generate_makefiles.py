#!/usr/bin/env python2.7
import random

sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

for sz in sizes:
    with open('makefile-{}'.format(sz), 'w+') as f:
        nums = range(1, sz)
        random.shuffle(nums)
        for i in nums:
            f.write('a{}: a{}\n'.format(i, i+1))
            f.write('\techo {}\n'.format(i))
            f.write('\n')
        f.write('a{}:\n'.format(sz))
        f.write('\techo {}\n'.format(sz))
