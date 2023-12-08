#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:04:04 2023

@author: robertnolet
"""

value = {'A':14,'K':13,'Q':12,'J':11,'T':10} | {str(i):i for i in range(2,10)}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.s = max(hand.count(c) for c in hand) # Longest streak
        self.l = len(set(hand))                   # Number unique

    def __lt__(self, other):
        if self.s != other.s:
            return self.s < other.s
        if self.s in [2,3] and self.l != other.l:
            # s == 2: (one pair, two pairs) or s == 3: (full house, three of a kind)
            return self.l > other.l
        # Hands are both same type
        return tuple(value[c] for c in self.hand) < tuple(value[c] for c in other.hand)

    def switchpart2(self):
        j = sum(c == 'J' for c in self.hand)
        if j == 5:
            self.s = 5
            self.l = 1
        else:
            self.s = max(self.hand.count(c) for c in self.hand if c != 'J') + j
            self.l -= (j > 0)


data = [Hand(line[:5], int(line[6:])) for line in open('input.txt')]

print('Part 1:', sum((v+1)*h.bid for v, h in enumerate(sorted(data))))

value['J'] = 0
for hand in data:
    hand.switchpart2()

print('Part 2:', sum((v+1)*h.bid for v, h in enumerate(sorted(data))))
