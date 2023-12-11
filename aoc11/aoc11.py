#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:20:57 2023

@author: robertnolet
"""

import numpy as np
from itertools import combinations

data = np.array([list(line.strip()) for line in open('input.txt')])
n,m = data.shape

emptyrows = [i for i in range(n) if np.all(data[i,:] == '.')]
emptycols = [j for j in range(m) if np.all(data[:,j] == '.')]
stars = np.argwhere(data == '#')

def dist(i1,j1,i2,j2, mul=2):
    di = abs(i2-i1) + (mul-1)*sum(min(i1,i2) < r < max(i1,i2) for r in emptyrows)
    dj = abs(j2-j1) + (mul-1)*sum(min(j1,j2) < c < max(j1,j2) for c in emptycols)
    return di+dj

print('Part 1:', sum(dist(*s1,*s2) for s1, s2 in combinations(stars,2)))
print('Part 2:', sum(dist(*s1,*s2, 1000000) for s1, s2 in combinations(stars,2)))
