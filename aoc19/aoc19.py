#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:17:19 2023

@author: robertnolet
"""

import re
from math import prod

def parsewflow(s):
    i = s.index('{')
    name = s[:i]
    parts = s[i+1:-1].split(',')
    rules = []
    for part in parts[:-1]:
        var, op, value, dest = pat1.match(part).groups()
        rules.append((var, op, int(value), dest))
    return name, rules, parts[-1]


pat1 = re.compile(r'([xmas])([<>])(\d+):(\w+)')
pat2 = re.compile(r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}')

p1, p2 = open('input.txt').read().split('\n\n')
wflows = {name:(rules, final) for name, rules, final in map(parsewflow, p1.split('\n'))}
parts = [{c:int(v) for c, v in zip('xmas', pat2.match(s).groups())} for s in p2.split('\n')]


def apply(rules, final, part):
    for var, op, value, dest in rules:
        if op == '<' and part[var] < value:
            return dest
        if op == '>' and part[var] > value:
            return dest
    return final

def count(wf, ranges):
    if any(e < s for s, e in ranges.values()):
        return 0
    if wf == 'A':
        return prod(e-s+1 for s, e, in ranges.values())
    if wf == 'R':
        return 0
        
    result = 0
    rules, final = wflows[wf]
    for var, op, value, dest in rules:
        s, e = ranges[var]
        if op == '<' and s < value:
            ranges[var] = (s, min(e, value-1))
            result += count(dest, ranges.copy())
            if e < value:
                return result
            ranges[var] = (value, e)
        if op == '>' and e > value:
            ranges[var] = (max(s, value+1), e)
            result += count(dest, ranges.copy())
            if s > value:
                return result
            ranges[var] = (s, value)
    result += count(final, ranges)
    return result
    

result = 0
for part in parts:
    wf = 'in'
    while wf not in ['A', 'R']:
        wf = apply(*wflows[wf], part)
    if wf == 'A':
        result += sum(part.values())
print('Part 1:', result)

ranges = {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}
print('Part 2:', count('in', ranges))