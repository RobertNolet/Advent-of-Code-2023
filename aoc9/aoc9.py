#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:08:34 2023

@author: robertnolet
"""

from math import comb

data = [[ int(s) for s in line.split()] for line in open('input.txt')]

result1 = 0
result2 = 0
n = len(data[0])
for line in data:
    derivs = [line[0]]
    while any(x != 0 for x in line):
        line = [line[i+1]-line[i] for i in range(len(line)-1)]
        derivs.append(line[0])
    result1 += sum(comb(n, i)*derivs[i] for i in range(len(derivs)))
    result2 += sum((-1)**i*derivs[i] for i in range(len(derivs)))

print('Part 1:', result1, ', Part 2:', result2)