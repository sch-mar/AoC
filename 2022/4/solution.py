#! /usr/bin python3

import time

inp = [[list(map(int, r.split('-'))) for r in l.split(',')] for l in open("input", "r").read().splitlines()[:-1]]

## PART 1

ans = 0
for t in inp:
    t.sort()
    if t[0][0] <= t[1][0] and t[0][1] >= t[1][1]:
        ans += 1
    elif t[1][0] <= t[0][0] and t[1][1] >= t[0][1]:
        ans += 1

print(f"In {ans} assignment pairs one range does fully contain the other")

## PART 2

ans = 0
for t in inp: #team
    t.sort(key=lambda x: max(x)-min(x))
    for i in range(t[0][0], t[0][1]+1):
        if i in range(t[1][0], t[1][1]+1):
            ans += 1
            break

print(f"In {ans} assignment pairs the ranges overlap")

