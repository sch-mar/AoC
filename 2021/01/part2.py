#!/usr/bin/env python3

meas = [int(i) for i in open("input").readlines()]
incs = 0

for i in range(3, len(meas)):
    if meas[i]+meas[i-1]+meas[i-2] > meas[i-1]+meas[i-2]+meas[i-3]:
        incs += 1

print(incs)

