#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:50:31 2023

@author: robertnolet
"""

def score(n):
    return 0 if n == 0 else 2**(n-1)


counts = []
for line in open('input.txt'):
    p1, p2 = line.split(':')    
    p2, p3 = p2.split('|')
    counts.append(len(set(map(int, p2.split())) & set(map(int, p3.split()))))
n = len(counts)

print('Part 1:', sum(map(score, counts)))

cards = [1]*n
for c in range(n):
    for i in range(counts[c]):
        cards[c+i+1]+=cards[c]

print('Part 2:', sum(cards))