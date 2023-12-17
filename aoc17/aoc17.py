#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 09:19:16 2023

@author: robertnolet
"""

import numpy as np

data = np.array([[int(c) for c in line.strip()] for line in open('input.txt')])
n, m = data.shape

dirs = {0: [(1,0), (-1,0)], # Vertical
        1: [(0,1), (0,-1)]} # Horizontal

def solve(steps):
    dist = 1000000000*np.ones((*data.shape,2), dtype=int)
    dist[0,0,:] = 0
    visited = np.zeros((*data.shape,2), dtype=int)
    visited[0,0,:] = 1
    
    tocheck = {(0,0,0),(0,0,1)}
    while True:
        dis, i, j, h = min((dist[i,j,h], i, j, h) for (i, j, h) in tocheck)
        if i == n-1 and j == m-1:
            return dis
        for di, dj in dirs[h]:
            newd = dis
            for s in range(1, steps[0]):
                 if 0 <= i+s*di < n and 0 <= j+s*dj < m:
                     newd += data[i+s*di,j+s*dj]
            for s in steps:
                 if 0 <= i+s*di < n and 0 <= j+s*dj < m:
                     newd += data[i+s*di,j+s*dj]
                     if not visited[i+s*di,j+s*dj,1-h]:
                         dist[i+s*di,j+s*dj,1-h] = min(dist[i+s*di,j+s*dj,1-h], newd)
                         tocheck.add((i+s*di,j+s*dj,1-h))
        tocheck.remove((i, j, h))
        visited[i,j,h] = 1

print('Part 1:', solve([1,2,3]))
print('Part 2:', solve([4, 5, 6, 7, 8, 9, 10]))