#! /usr/bin python3

## on 16GB RAM Notebook runs for some minutes

import re

inp = open("../../input/2022/15/input", 'r').read().splitlines()[:-1]

# sensor: beacon
reg = re.compile("-?\d+")
sb = {(l[0], l[1]): ((l[2], l[3]), abs(l[0]-l[2])+abs(l[1]-l[3])) for l in [list(map(int, re.findall(reg, l))) for l in inp]}
beacons = [(bx, by) for (sx, sy), ((bx, by), dist) in sb.items()]

## PART 1

xmin = min([sx - dist for (sx, sy), ((bx, by), dist) in sb.items()])
xmax = max([sx + dist for (sx, sy), ((bx, by), dist) in sb.items()])

y = 2000000
bp = [False for i in range(xmax - xmin)] # possible beacon positions
# size of list might be optimized, but probably not necessary

x = xmin
while x < xmax:
    count = 0
    if (x, y) not in beacons:
        for (sx, sy), ((bx, by), dist) in sb.items():
            while abs(sx - x) + abs(sy - y) <= dist:
                if (x, y) not in beacons:
                    bp[x - xmin] = True
                x += 1
                count += 1
    if not count:
        x += 1

print(f"In the row {y}, {bp.count(True)} positions might contain a beacon.")

## PART 2
ymin = min([sy - dist for (sx, sy), ((bx, by), dist) in sb.items()])
search_area = 4000000#20
rows = [set() for i in range(search_area + 1)]
for (sx, sy), ((bx, by), dist) in list(sb.items()):
    ## get endpoints of "beacon rhombus"
    # rhombus = ((sx, sy - dist), (sx + dist, sy), (sx, sy + dist), (sx - dist, sy))
    for i in range(dist):
        if sy + i <= search_area:
            rows[sy + i].add((sx - dist + i, sx + dist - i))
        if sy - i >= 0:
            rows[sy - i].add((sx - dist + i, sx + dist - i))
print("halftime")
for i, ranges in enumerate(list(map(sorted, rows.values()))):
    a = None
    b = None
    for r1, r2 in ranges:
        r1 = r1 if r1 >= 0 else 0
        r2 = r2 if r2 <= search_area else search_area
        if not b:
            a, b = r1, r2
        elif r1 <= b:
            if r2 > b:
                b = r2
        else:
            print(f"The tuning frequency is {(r1-1)*4000000+i}.")
            exit()


