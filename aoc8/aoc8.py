#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:42:00 2023

@author: robertnolet
"""

from math import lcm

lr = {'L':0, 'R':1}

with open('input.txt') as file:
    dirs = [lr[c] for c in file.readline().strip()]
    n = len(dirs)
    file.readline()
    data = {line[:3]:(line[7:10], line[12:15]) for line in file.readlines()}
    

def move(loc, step):
    return data[loc][dirs[step % n]]

    
step = 0
loc = 'AAA'
while loc != 'ZZZ':
    loc = move(loc, step)
    step += 1

print('Part 1:', step)

cycles = []
locs = [loc for loc in data if loc[2] == 'A']
zstep = {loc:[] for loc in locs}
for start in locs:
    step = 0
    visited = {loc:[] for loc in data}
    loc = start
    while all((step-s) % n != 0 for s in visited[loc]):
        if loc[2] == 'Z':
            zstep[start].append(step)
        visited[loc].append(step)
        loc = move(loc, step)
        step += 1
    s = next(s for s in visited[loc] if (step - s)%n == 0)
    cycles.append((loc, s, step, step-s))

print(zstep)
print(cycles)

# Oddly enough, each ghost reaches it's one Z location at step == cyclelength
# So we just need to find the least common multiple    
print('Part 2:', lcm(*[cycle[3] for cycle in cycles]))
