#! /usr/bin python3

def adjacent_coordinates(x, y, i, j): # size, coordinates
    a = []
    # top
    if i>0:
        a.append([i-1, j])
        # top left
        if j>0:
            a.append([i-1, j-1])
        # top right
        if j<y-1:
            a.append([i-1, j+1])
    # left
    if j>0:
        a.append([i, j-1])
    # right
    if j<y-1:
        a.append([i, j+1])
    # bottom
    if i<x-1:
        a.append([i+1, j])
        # bottom left
        if j>0:
            a.append([i+1, j-1])
        # bottom right
        if j<y-1:
            a.append([i+1, j+1])
    return a # list of adjacent coordinates

def increase_energy(o, n): # increase energy on o by n
    for i in range(len(o)):
        for j in range(len(o[i])):
            o[i][j] += 1
    return

def check_flashes(o, n, flashed): # check o for flashes (value>n) thaht have not been flashed yet (flashed)
    f = []
    for i in range(len(o)):
        for j in range(len(o[i])):
            if o[i][j]>n and [i, j] not in flashed:
                f.append([i, j])
                flashed.append([i, j])
    return f # flash coordinates

def flash_o(o, flash, n, m): # set values in flash/o to n, increase adjacent values by m
    c = 0
    for i, j in flash:
        o[i][j] = n
        adj = adjacent_coordinates(len(o), len(o[0]), i, j)
        for q, r in adj:
            if o[q][r]>0:
                o[q][r] += m
        c += 1
    return c # number of flashes

from textwrap import wrap

inp = [list(map(int, wrap(l.strip("\n"), 1))) for l in open("input").readlines()]

## PART 1

o1 = inp.copy() # octopus' for part 1
flashed = [] # list of already flashed octopuses'
flash = [] # list of flashing o's
sf1 = 0 # sum of flashes

for i in range(100):
    flashed.clear()
    increase_energy(o1, 1)
    flash = check_flashes(o1, 9, flashed)
    while len(flash)>0:
        sf1 += flash_o(o1, flash, 0, 1)
        flash = check_flashes(o1, 9, flashed)

print(f"{sf1} flashes occured.")

## PART 2

o2 = [list(map(int, wrap(l.strip("\n"), 1))) for l in open("input").readlines()]
sf2 = 0 # sum of flashes per step
c2 = 0 # counter of steps

while sf2!=100:
    c2 += 1
    sf2 = 0
    flashed.clear()
    increase_energy(o2, 1)
    flash = check_flashes(o2, 9, flashed)
    while len(flash)>0:
        sf2 += flash_o(o2, flash, 0, 1)
        flash = check_flashes(o2, 9, flashed)

print(f"All Octopuses flash simultaneously first at step {c2}.")

