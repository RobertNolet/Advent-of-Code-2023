#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:04:27 2023

@author: robertnolet
"""

from math import prod

def parseset(line):
    s = {}
    for cube in line.split(','):
        v, c = cube.strip().split(' ')
        s[c] = int(v)
    return s

bag = {'red':12, 'green':13, 'blue':14}

def possibleset(s):
    return all(v <= bag[c] for c, v in s.items())

def possiblegame(game):
    return all(possibleset(s) for s in game)

def power(game):
    return prod(max(s.get(c,1) for s in game) for c in bag)

games = {}
for line in open('input.txt'):
    p1, p2 = line.split(':')
    games[int(p1[5:])] = [parseset(s) for s in p2.split(';')]

print('Part 1:', sum(i for i in games if possiblegame(games[i])))

print('Part 2:', sum(power(games[i]) for i in games))