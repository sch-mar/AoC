#! /usr/bin python3

################################
# Solution inspired by @joshbduncan
# [Reddit profile](https://www.reddit.com/user/joshbduncan/)
# [Code source](https://www.reddit.com/r/adventofcode/comments/zkmyh4/comment/j0cgmkb/?utm_source=share&utm_medium=web2x&context=3)
################################

from ast import literal_eval
from functools import cmp_to_key
from math import prod

def compare(l, r):
    # make sure l, r are lists
    l = l if isinstance(l, list) else [l]
    r = r if isinstance(r, list) else [r]
    # iterate over each packet part
    for ll, rr in zip(l, r):
        # if at least one part is a list
        if isinstance(ll, list) or isinstance(rr, list):
            # compare parts
            c = compare(ll, rr)
        else:
            # calculate difference (because both are integers)
            c = rr - ll
        # if difference not null correct/incorrect order is found
        if c != 0:
            return c
    # if no difference has come up yet, return difference in part length
    return len(r) - len(l)

inp = open("../../input/2022/13/input", 'r').read().splitlines()[:-1]

## PART 1
pairs = [list(map(literal_eval, [inp[i], inp[i+1]])) for i in range(0, len(inp), 3)] # pairs of packets as lists
print(f"The sum of the indices of the correct pairs is {sum([i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) > 0])}.")

## PART 2
# list of packets not as pairs and divider packets
packets = sorted([y for x in pairs for y in x] + [[[6]]] + [[[2]]], key=cmp_to_key(compare), reverse=True)
print(f"The decoder key for the distress signal is {prod([i for i, p in enumerate(packets, 1) if p in [[[6]], [[2]]]])}.")

