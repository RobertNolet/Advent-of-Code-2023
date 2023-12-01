#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:55:15 2023

@author: robertnolet
"""

import re

data = [s.strip() for s in open('input.txt')]

# Part 1
digits = [[int(c) for c in s if c.isdigit()] for s in data]
print('Part 1:', sum(10*x[0]+x[-1] for x in digits))

# Part 2
subs = {'one':'1',
        'two': '2',
        'three':'3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}

def value(m):
    return int(subs.get(m, m))

ws = 'one|two|three|four|five|six|seven|eight|nine'
pat = re.compile(ws+'|[0-9]')
res = 10*sum(value(pat.search(s).group(0)) for s in data)
        
pat = re.compile(ws[::-1]+'|[0-9]')
res += sum(value(pat.search(s[::-1]).group(0)[::-1]) for s in data)
print('Part 2:', res)