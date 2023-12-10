#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:56:04 2023

@author: robertnolet
"""


pipes = {'|':{(-1, 0),(+1, 0)},
         '-':{( 0,+1),( 0,-1)},
         'L':{(-1, 0),( 0,+1)},
         'J':{( 0,-1),(-1, 0)},
         '7':{( 0,-1),(+1, 0)},
         'F':{( 0,+1),(+1, 0)},
         '.':set()}

data = [line.strip() for line in open('input.txt')]
n = len(data)
m = len(data[0])

i, j = next((i,j) for i in range(n) for j in range(m) if data[i][j] == 'S')
for t, ds in pipes.items():
    if all((-di,-dj) in pipes[data[i+di][j+dj]] for (di,dj) in ds):
        starttile = t
        break
di, dj = next(iter(pipes[starttile]))    # Ewww, but popping destroys pipes

loop = {(i,j)}
i += di
j += dj
while data[i][j] != 'S':
    loop.add((i,j))
    di, dj = (pipes[data[i][j]] - {(-di, -dj)}).pop()
    i += di
    j += dj
    
print('Part 1:', len(loop)//2)

opps = {'L':'7', 'F':'J'}

area = 0
for i in range(n):
    inside = False
    for j in range(m):
        tile = data[i][j] if data[i][j] != 'S' else starttile
        if (i,j) in loop:
            if tile in 'LF':
                start = tile
            elif tile == '|' or tile == opps[start]:
                inside = not inside
        elif inside:
            area += 1
                
print('Part 2:', area)