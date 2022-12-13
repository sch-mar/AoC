#! /usr/bin python3

## PART 1

inp = [str(l).strip("\n") for l in open("input").readlines()]

# transform input

vents = []

for a in [l.replace(" -> ", ";").split(";") for l in inp]:
    vents.append([list(map(int, a[0].split(","))), list(map(int, a[1].split(",")))])

#vents = list(map(int, vents))

# calculate vents

#fvents = [] # all coordinates of each vent
#fvc = 0 # counter
d = 0 # distance

for v in vents:
    if v[0][0]!=v[1][0] and v[0][1]!=v[1][1]: # diagonal
        continue # ignore diagonal vents
    if v[0][0]!=v[1][0]:# x/col
        d = v[1][0]-v[0][0]
        if abs(d)>1:
            for i in range(1, abs(d)):
                v.insert(i, [v[0][0]+int(i*(d/abs(d))), v[0][1]])
    else: # y/row
        d = v[1][1]-v[0][1]
        if abs(d)>1:
            for i in range(1, abs(d)):
                v.insert(i, [v[0][0], v[0][1]+int(i*(d/abs(d)))])

# calculate map

vmap = [[0 for j in range(1000)] for i in range(1000)]

for v in vents:
    if v[0][0]!=v[1][0] and v[0][1]!=v[1][1]: # diagonal
        continue # ignore diagonal vents
    else:
        for c in v:
            vmap[c[1]][c[0]]+=1

# check map

c1 = 0 # counter

for r in vmap:
    for c in r:
        if c>=2:
            c1+=1

print(f"Amount of dangerous points(without diagonals): {c1}")

## PART 2

# calculate missing diagonal vents

d = 0 # distance
xsign = 0
ysign = 0

for v in vents:
    if v[0][0]!=v[1][0] and v[0][1]!=v[1][1]: # diagonal
        d=v[1][0]-v[0][0]
        if abs(d)>1:
            xsign = d/abs(d) # x used to calculate distance
            ysign = (v[1][1]-v[0][1])/abs(v[1][1]-v[0][1])
            for i in range(1, abs(d)):
                    v.insert(i, [v[0][0]+int(i*xsign), v[0][1]+int(i*ysign)])

# calculate map

vmap = [[0 for j in range(1000)] for i in range(1000)]

for v in vents:
    for c in v:
        vmap[c[1]][c[0]]+=1

# check map

c2 = 0 # counter

for r in vmap:
    for c in r:
        if c>=2:
            c2+=1

print(f"Amount of dangerous points(with diagonals): {c2}")



