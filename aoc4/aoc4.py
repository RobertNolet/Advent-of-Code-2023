#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:50:31 2023

@author: robertnolet
"""

def score(n):
    return 0 if n == 0 else 2**(n-1)

data = [(set(map(int, p.split())) for p in line.split(':')[1].split('|')) for line in open('input.txt')]
counts = [len(x&y) for x,y in data]

print('Part 1:', sum(map(score, counts)))

cards = [1]*len(data)
for c in range(len(data)):
    for i in range(counts[c]):
        cards[c+i+1]+=cards[c]

print('Part 2:', sum(cards))