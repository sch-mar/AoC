#! /usr/bin python3

import json

def calc_size(d, sizes={}, path=[]):
    if dict not in set([type(val) for val in d.values()]): # branch, no sub dir
        return sum(d.values())
    for key in d:
        if type(d[key]) is dict:
            path.append(key)
            sizes['/' + '/'.join(path)] = calc_size(d[key], sizes, path.copy())
    size = 0
    for key in d:
        if type(d[key]) is dict:
            size += sizes['/' + '/'.join(path)]
        else:
            size += d[key]
    return size


inp = [l.split() for l in open("input", "r").readlines()[:-1]]

## input parsing

tree = {}
subtree = tree
path = []
sizes = {}
for l in inp:
    if l[0] == '$': #command
        if l[1] == 'cd':
            if l[2] == '/': # move to root
                path = []
            elif l[2] == '..': # move out
                path.pop()
            else: # move in
                path.append(l[2])
        else: # ls
            # loop to set subtree to path
            # subtree = tree
            for i, key in enumerate(path):
                if not i: # first level
                    subtree = tree.setdefault(key) # depends on existing dir
                else:
                    subtree = subtree.setdefault(key)
    else: # file/dir
        if l[0] == 'dir':
            subtree[l[1]] = {}
        else: # file
            subtree[l[1]] = int(l[0])
            # sizes
            curpath = ""
            for p in ['/'] + path:
                curpath += "/" + p.strip('/')
                sizes[curpath] = sizes.get(curpath, 0) + int(l[0])

# sizes = {}
# sizes['/'] = calc_size(tree, sizes)
# json.dump(tree, open("tree.json", "w"), indent=4)
# json.dump(sizes, open("sizes.json", "w"), indent=4)

## PART 1

print(f"The total sum of those directories is {sum([s for s in sizes.values() if s <= 100000])}")

## PART 2
free_space = 70000000 - sizes['/']
for s in sorted(sizes.values()):
    if free_space + s >= 30000000:
        print(s)
        break



