#! /usr/bin python3 

from textwrap import wrap

def check_lowpoint(i, j, c): # i, j, coordinates list
    v = c[i][j] # value
    # top
    if i-1>=0:
        if c[i-1][j]<=v:
            return False
    # right
    if j+1<len(c[i]):
        if c[i][j+1]<=v:
            return False
    # bottom
    if i+1<len(c):
        if c[i+1][j]<=v:
            return False
    # left
    if j-1>=0:
        if c[i][j-1]<=v:
            return False
    return True

def check_basin(i, j, b, c): # coordinates of point, basin (coordinates), input
    # top
    if i-1>=0:
        if c[i-1][j]<9 and [i-1, j] not in b:
            b.append([i-1, j])
    # right
    if j+1<len(c[i]):
        if c[i][j+1]<9 and [i, j+1] not in b:
            b.append([i, j+1])
    # bottom
    if i+1<len(c):
        if c[i+1][j]<9 and [i+1, j] not in b:
            b.append([i+1, j])
    # left
    if j-1>=0:
        if c[i][j-1]<9 and [i, j-1] not in b:
            b.append([i, j-1])

## PART 1

inp = [list(map(int, wrap(l.strip("\n"), 1))) for l in open("input").readlines()]

# find lowpoints

lp = [] # lowpoints coordinates

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if check_lowpoint(i, j, inp):
            lp.append([i, j])

# calculate risklevel

sum = 0

for p in lp:
    sum += inp[p[0]][p[1]] + 1

print(f"sum of risklevels is {sum}.")

## PART 2

b = [] # basin
bs = [] # basin sizes
bc = 0 #basincounter

for p in lp:
    b = [[p[0], p[1]]]
    bc = 0
    while bc<len(b): # and bc<10:
        check_basin(b[bc][0], b[bc][1], b, inp)
        bc += 1
    bs.append(len(b))

bs.sort()

print(f"Multiplying the sizes of the three biggest basins gets you {bs[-1]*bs[-2]*bs[-3]}")

