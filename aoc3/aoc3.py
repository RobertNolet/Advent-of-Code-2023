#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:01:07 2023

@author: robertnolet
"""

data = [line.strip() for line in open('input.txt')]

n = len(data)
m = len(data[0])

def valid(i,j):
    return (0 <= i < n) and (0 <= j < m)

def ispart(i,j):
    return valid(i,j) and data[i][j] != '.' and not data[i][j].isdigit()

def isgear(i,j):
    return valid(i,j) and data[i][j] == '*'

gears = {}
result1 = 0
result2 = 0
for i in range(n):
    j=0
    while (j<m):
        v=0
        part = False
        gear = []
        while (j < m) and not data[i][j].isdigit():
            j += 1
        # Left
        for di in [-1,0,1]:
            if ispart(i+di,j-1):
                part = True
            if isgear(i+di,j-1):
                gear.append((i+di,j-1))
        while (j < m) and data[i][j].isdigit():
            v = 10*v + int(data[i][j])
            # Top and Bottom
            if ispart(i-1,j) or ispart(i+1,j):
                part = True
            if isgear(i-1,j):
                gear.append((i-1,j))
            if isgear(i+1,j):
                gear.append((i+1,j))
            j += 1
        # Right
        for di in [-1,0,1]:
            if ispart(i+di,j):
                part = True
            if isgear(i+di,j):
                gear.append((i+di,j))
        if part:
            result1 += v
        for g in gear:
            if g in gears:
                result2 += gears[g] * v
            else:
                gears[g] = v

print('Part 1:', result1)
print('Part 2:', result2)