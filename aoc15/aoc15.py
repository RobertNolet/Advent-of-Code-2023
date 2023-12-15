#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:52:30 2023

@author: robertnolet
"""


def makehash(s):
    return sum(ord(c)*(17**(len(s)-i)) for i, c in enumerate(s))%256

# data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')
data = open('input.txt').readline().split(',')

print('Part 1:', sum(makehash(s) for s in data))

lenses = [[] for j in range(256)]
focals = [[] for j in range(256)]

for s in data:
    if s[-1] == '-':
        s = s[:-1]
        i = makehash(s)
        if s in lenses[i]:
            j = lenses[i].index(s)
            lenses[i].pop(j)
            focals[i].pop(j)
    else:
        s, v = s.split('=')
        i = makehash(s)
        if s in lenses[i]:
            j = lenses[i].index(s)
            focals[i][j] = int(v)
        else:
            lenses[i].append(s)
            focals[i].append(int(v))
        
    
print('Part 2:', sum((i+1)*(j+1)*v for i, foc in enumerate(focals) for j,v in enumerate(foc)))