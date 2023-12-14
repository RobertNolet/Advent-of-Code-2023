#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:18:48 2023

@author: robertnolet
"""

data = [list(line.strip()) for line in open('input.txt')]
n = len(data)
m = len(data[0])


def north(data):
    load = 0
    rows = [0]*m
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'O':
                data[i][j] = '.'
                data[rows[j]][j] = 'O'
                load += n-rows[j]
                rows[j] += 1
            elif data[i][j] == '#':
                rows[j] = i+1
    return load

def west(data):
    cols = [0]*n
    for j in range(m):
        for i in range(n):
            if data[i][j] == 'O':
                data[i][j] = '.'
                data[i][cols[i]] = 'O'
                cols[i] += 1
            elif data[i][j] == '#':
                cols[i] = j+1


def south(data):
    rows = [n-1]*m
    for i in range(n-1,-1,-1):
        for j in range(m):
            if data[i][j] == 'O':
                data[i][j] = '.'
                data[rows[j]][j] = 'O'
                rows[j] -= 1
            elif data[i][j] == '#':
                rows[j] = i-1

def east(data):
    load = 0
    cols = [m-1]*n
    for j in range(m-1,-1,-1):
        for i in range(n):
            if data[i][j] == 'O':
                data[i][j] = '.'
                data[i][cols[i]] = 'O'
                cols[i] -= 1
                load += n-i
            elif data[i][j] == '#':
                cols[i] = j-1
    return load

def asstr(data):
    return '\n'.join(''.join(line) for line in data)
    

def runcycles(data, count = 1000000000):
    loads = {}
    for i in range(count):
        north(data)
        west(data)
        south(data)
        load = east(data)
        if asstr(data) in loads:
            return i, loads[asstr(data)]
        loads[asstr(data)] = i
    print('Part 2:', load)
    
load = north(data)
print('Part 1:', load)

data = [list(line.strip()) for line in open('input.txt')]
i, j = runcycles(data)
runcycles(data, (1000000000-j-1)%(i-j))

            