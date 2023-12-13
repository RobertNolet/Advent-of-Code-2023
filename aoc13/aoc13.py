#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:18:46 2023

@author: robertnolet
"""

import numpy as np


def reflectonrow(b, i, smudge):
    s = i - min(b.shape[0]-i, i)
    e = i + min(b.shape[0]-i, i)
    return np.sum(b[s:i, :] != b[e-1:i-1:-1, :]) == smudge


def reflectoncol(b, j, smudge):
    s = j - min(b.shape[1]-j, j)
    e = j + min(b.shape[1]-j, j)
    return np.sum(b[:, s:j] != b[:, e-1:j-1:-1]) == smudge


def score(b, smudge):
    return (sum(i for i in range(1, b.shape[0]) if reflectonrow(b, i, smudge))*100 +
            sum(j for j in range(1, b.shape[1]) if reflectoncol(b, j, smudge)))


data = [np.array([list(s) for s in b.split('\n')]) for b in open('input.txt').read().split('\n\n')]
print('Part 1:', sum(score(b, 0) for b in data))
print('Part 2:', sum(score(b, 1) for b in data))
