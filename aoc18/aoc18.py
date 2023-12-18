#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:54:40 2023

@author: robertnolet
"""

import numpy as np

dirs = {'R':0,'D':1,'L':2,'U':3}
data = np.array([(dirs[d], int(v), int(col[7]), int(col[2:7], base=16)) for d, v, col in map(str.split, open('input.txt'))])

def solve(dat):
    area = 0
    i = 0
    for d, v in dat:
        if d == 0:
            i += v
        elif d == 1:
            area += v*i
        elif d == 2:
            i -= v
            area += v
        elif d == 3:
            area -= v*(i-1)
    return area+1

print('Part 1:', solve(data[:,:2]))
print('Part 2:', solve(data[:,2:]))