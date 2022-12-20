#! /usr/bin python3

from itertools import zip_longest

inp = open("../../input/2022/14/input", 'r').read().splitlines()[:-1]

# rock structures
rocks = []
for l in inp:
    rocks.append([])
    for e in l.split(" -> "):
        rocks[-1].append(list(map(int, e.split(','))))

# build map
xmin = min([x[0] for r in rocks for x in r])
xmax = max([x[0] for r in rocks for x in r])
ymax = max([x[1] for r in rocks for x in r])
rmap = [['.' for i in range(xmax - xmin + 1)] for l in range(ymax + 1)]

# normalize rock coordinates
norm = -xmin # normalizer
for rock in rocks:
    for coordinates in rock:
        coordinates[0] += norm
# convert coordinates to tuples
rocks = [list(map(tuple, rock))for rock in rocks]

# draw rocks in map
for rock in rocks:
    for (x1, y1), (x2, y2) in zip(rock[:-1], rock[1:]):# column, row
        x_list = [i for i in range(sorted([x1, x2])[0], sorted([x1, x2])[1] + 1)]
        y_list = [i for i in range(sorted([y1, y2])[0], sorted([y1, y2])[1] + 1)]
        for x, y in zip_longest(x_list, y_list, fillvalue=sorted([x_list, y_list], key=len)[0][0]):
            rmap[y][x] = '#'

## PART 1
ENTRY = [500 + norm, 0] # sand entry point
sand = 0
void = False
while not void:
    sand_unit = list(ENTRY)
    while True:
        if sand_unit[1] == len(rmap) -1 or sand_unit[0] == 0 or sand_unit[0] == len(rmap[0]) - 1: # sand flow into void
            void = True
            break
        elif rmap[sand_unit[1] + 1][sand_unit[0]] == '.':
            sand_unit[1] += 1
        elif sand_unit[0] > 0 and rmap[sand_unit[1] + 1][sand_unit[0] - 1] == '.':
            sand_unit[1] += 1
            sand_unit[0] -= 1
        elif sand_unit[0] < len(rmap[0]) - 1 and rmap[sand_unit[1] + 1][sand_unit[0] + 1] == '.':
            sand_unit[1] += 1
            sand_unit[0] += 1
        else:
            rmap[sand_unit[1]][sand_unit[0]] = 'o'
            sand += 1
            break

print(f"The sand stops flowing into the abyss after {sand} sand units.")

## PART 2
# add empty row to rocks
rmap.append(['.' for i in range(xmax - xmin + 1)])
# add floor to rocks
rmap.append(['#' for i in range(xmax - xmin + 1)])

while rmap[ENTRY[1]][ENTRY[0]] == '.':
    sand_unit = list(ENTRY)
    while True:
        # expand map
        if sand_unit[0] == 0:
            # expand left
            for l in rmap:
                l = l.insert(0, '.')
            rmap[-1][0] = '#'
            # adjust coordinates
            norm -= 1
            sand_unit[0] += 1
            ENTRY[0] += 1
        elif sand_unit[0] == len(rmap[0]) - 1:
            # expand right
            for l in rmap:
                l.append('.')
            rmap[-1][-1] = '#'
        # move sand unit
        if rmap[sand_unit[1] + 1][sand_unit[0]] == '.':
            sand_unit[1] += 1
        elif sand_unit[0] > 0 and rmap[sand_unit[1] + 1][sand_unit[0] - 1] == '.':
            sand_unit[1] += 1
            sand_unit[0] -= 1
        elif sand_unit[0] < len(rmap[0]) - 1 and rmap[sand_unit[1] + 1][sand_unit[0] + 1] == '.':
            sand_unit[1] += 1
            sand_unit[0] += 1
        else:
            rmap[sand_unit[1]][sand_unit[0]] = 'o'
            sand += 1
            break
    if sand_unit == list(ENTRY):
        rmap[sand_unit[1]][sand_unit[0]] = 'o'

print(f"{sand} units of sand come to rest.")
