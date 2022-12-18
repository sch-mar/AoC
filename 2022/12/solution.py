#! /usr/bin python3

def adjacent(v, hm, limit=1): # base pos, map, maximum difference (1 means adj is 1 higher than v)
    adj = []
    if v[1] > 0: # left
        if hm[v[0]][v[1] - 1] - hm[v[0]][v[1]] <= limit:
            adj.append((v[0], v[1] - 1))
    if v[1] < len(hm[0]) - 1: # right
        if hm[v[0]][v[1] + 1] - hm[v[0]][v[1]] <= limit:
            adj.append((v[0], v[1] + 1))
    if v[0] > 0: # top
        if hm[v[0] - 1][v[1]] - hm[v[0]][v[1]] <= limit:
            adj.append((v[0] - 1, v[1]))
    if v[0] < len(hm) - 1: # bottom
        if hm[v[0] + 1][v[1]] - hm[v[0]][v[1]] <= limit:
            adj.append((v[0] + 1, v[1]))
    return adj

inp = open("../../input/2022/12/input", 'r').read().splitlines()[:-1]

# build heightmap

hm = []
pos = {}
rc = 0 # counters
for r in inp:
    cc = 0
    hm.append([])
    for c in r:
        if c in ['S', 'E']:
            pos[c] = (rc, cc)
            hm[-1].append({'S': 0, 'E': 25}[c])
        else:
            hm[-1].append(ord(c) - 97)
        cc += 1
    rc += 1

## PART 1
q = [pos['S']] # queue
explored = [(pos['S'])]
tree = {} # {(coordinates): (parent coordinates)}
while q:
    v = q.pop(0)
    if v == pos['E']:
        break
    else:
        for a in adjacent(v, hm):
            if a not in explored:
                explored.append(a)
                tree[a] = v
                q.append(a)

n = pos['E']
path = []
while n != pos['S']: # build path from E to S
    path.append(n)
    n = tree[n]

print(f"The best signal is {len(path)} steps away.")

## PART 2

start_pos = {} # possible starting positions
rc = 0
for r in hm:
    cc = 0
    for c in r:
        if hm[rc][cc] == 0:
            start_pos[(rc, cc)] = -1
            cc += 1
    rc += 1

for sp in start_pos:
    q = [sp]
    explored = [sp]
    tree = {}
    while q:
        v = q.pop(0)
        if v == pos['E']:
            break
        else:
            for a in adjacent(v, hm):
                if a not in explored:
                    explored.append(a)
                    tree[a] = v
                    q.append(a)
    if pos['E'] not in tree.keys():
        start_pos.pop(sp)
        continue
    
    n = pos['E']
    path = []
    while n != sp:
        path.append(n)
        n = tree[n]
    start_pos[sp] = len(path)

print(f"The fewest steps required to move starting from any square with elevation a to the location that should get the best signal is {min(start_pos.values())}.")
    

