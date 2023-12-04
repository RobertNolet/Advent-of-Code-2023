#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:50:31 2023

@author: robertnolet
"""

def score(n):
    return 0 if n == 0 else 2**(n-1)


data = []
for line in open('input.txt'):
    p1, p2 = line.split(':')    
    p2, p3 = p2.split('|')
    data.append((set(map(int, p2.split())), set(map(int, p3.split()))))
n = len(data)

counts = [len(x&y) for x, y in data]

print('Part 1:', sum(map(score, counts)))

result = 0
cards = [1]*n
for c in range(n):
    for i in range(counts[c]):
        cards[c+i+1]+=cards[c]

print('Part 2:', sum(cards))