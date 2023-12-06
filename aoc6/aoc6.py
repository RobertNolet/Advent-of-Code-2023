#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:26:02 2023

@author: robertnolet
"""

from math import ceil, floor, sqrt, prod


def solverace(t, d):
    return floor((t + sqrt(t*t-4*d))/2) - ceil((t - sqrt(t*t-4*d))/2) + 1


with open('input.txt') as file:
    times = [int(s) for s in file.readline().split()[1:]]
    dists = [int(s) for s in file.readline().split()[1:]]

print('Part 1:', prod(solverace(t, d+1) for t, d in zip(times, dists)))
print('Part 2:', solverace(int(''.join(map(str, times))), int(''.join(map(str, dists)))+1))
