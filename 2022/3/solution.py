#! /user/bin python3

import string

def priority(i):
    if i in string.ascii_lowercase:
        return ord(i) - 96
    else:
        return ord(i) - 64 + 26

inp = open("input", "r").read().splitlines()[:-1]                                                  

## PART 1
items = []
for r in inp: #rucksacks
    done = []
    r = [r[:int(len(r)/2)], r[int(len(r)/2):]] # split into compartments
    for i in list(r[0]): # items
        if i in r[1] and i not in done:
            items.append(priority(i))
            done.append(i)

print(f"The sum is {sum(items)}.")

## PART 2

items = []
inp = [[inp[i], inp[i+1], inp[i+2]] for i in range(0, len(inp), 3)]
for g in inp: # groups
    g.sort(key=len)
    for i in g[0]:
        if i in g[1] and i in g[2]:
            items.append(priority(i))
            break

print(f"The sum is {sum(items)}.")

