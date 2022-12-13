#!/usr/bin/env python3

#meas = open("input.txt").read().split()
meas = [int(i) for i in open("input").readlines()]
incs = 0

for i in range(1, len(meas)):
    if meas[i] > meas[i-1]:
        incs += 1

print(incs)

