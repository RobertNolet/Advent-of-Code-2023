#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:20:29 2023

@author: robertnolet
"""

from itertools import batched

def solve(seedranges, data):
    for maps in data:
        newseedranges = []
        while seedranges:
            start, end = seedranges.pop()
            for dst, src, rng in maps:
                if src <= start and end < src+rng:
                    # Entire range gets mapped
                    newseedranges.append((dst + start - src, dst + end - src))
                    break
                if src <= start < src+rng and src+rng <= end:
                    # Left part gets mapped
                    newseedranges.append((dst + start - src, dst + rng))
                    seedranges.append((src+rng, end))
                    break
                if start < src and src < end < src+rng:
                    # Right part gets mapped
                    newseedranges.append((dst, dst + end - src))
                    seedranges.append((start, src))
                    break
                if start < src and src+rng <= end:
                    # Middle part gets mapped
                    newseedranges.append((dst, dst+rng))
                    seedranges.append((start, src))
                    seedranges.append((src+rng, end))
                    break
            else:
                # Range is not in any map
                newseedranges.append((start, end))
        seedranges = newseedranges
    return min(seedranges)[0]


def parsemap(block):
    return [[int(s) for s in line.split()] for line in block.split('\n')[1:]]


with open('input.txt') as file:
    seeds = [int(s) for s in file.readline().split()[1:]]
    file.readline()
    data = [parsemap(block) for block in file.read().split('\n\n')]


seedranges = [(seed, seed+1) for seed in seeds]
print('Part 1:', solve(seedranges, data))

seedranges = [(seed, seed+rng) for seed, rng in batched(seeds, 2)]
print('Part 2:', solve(seedranges, data))