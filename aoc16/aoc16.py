#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 07:46:29 2023

@author: robertnolet
"""

import numpy as np

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
R = 0
D = 1
L = 2
U = 3
turns = {'\\': [D, R, U, L],
         '/':  [U, L, D, R]}


data = np.array([list(line.strip()) for line in open('input.txt')])
n, m = data.shape

def beam(i, j, d, ener):
    while 0 <= i < n and 0 <= j < m:
        if ener[i,j,d] == 1:
            break
        ener[i,j,d] = 1
        if data[i,j] in '\\/':
            d = turns[data[i,j]][d]
        elif data[i,j] == '|' and d in [L, R]:
            beam(i+1, j, D, ener)
            beam(i-1, j, U, ener)
            break
        elif data[i,j] == '-' and d in [U, D]:
            beam(i, j+1, R, ener)
            beam(i, j-1, L, ener)
            break
        di, dj = dirs[d]
        i += di
        j += dj


def solve(i, j, d):
    ener = np.zeros((*data.shape, 4), dtype=int)
    beam(i, j, d, ener)
    return np.sum(ener.sum(axis=2) != 0)

print('Part 1:', solve(0,0,R))

tiles = []
for i in range(n):
    tiles.append(solve(i,0,R))
    tiles.append(solve(i,m-1,L))
for j in range(m):
    tiles.append(solve(0,j,D))
    tiles.append(solve(n-1,j,U))
print('Part 2:', max(tiles))
        
    
    
    