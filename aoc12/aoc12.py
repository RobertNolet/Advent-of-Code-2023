#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:15:50 2023

@author: robertnolet
"""

from itertools import combinations
from functools import cache

def parse(line):
    p1, p2 = line.split()
    return (p1, tuple(int(s) for s in p2.split(',')))

def valid(s, cts):
    return tuple(len(b) for b in s.split('.') if len(b) != 0) == cts


@cache
def count(s, cts):
    if len(cts) == 0:
        return s.count('#') == 0
    if len(s) < sum(cts) + len(cts)-1 or s.count('#') + s.count('?') < sum(cts):
        return 0
    if s.count('#') + s.count('?') == sum(cts):
        return valid(s.replace('?', '#'), cts)
    if all(c in '?#' for c in s[:cts[0]]) and s[cts[0]] != '#':
        result = count(s[cts[0]+1:], cts[1:])
    else:
        result = 0
    if s[0] != '#':
        result += count(s[1:], cts)
    return result

    
data = [parse(line) for line in open('input.txt')]
print('Part 1:', sum(count(s, cts) for s, cts in data))

data = [('?'.join([s]*5), cts*5) for s, cts in data]
print('Part 2:', sum(count(s, cts) for s, cts in data))
