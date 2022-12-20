#! /usr/bin python3

from ast import literal_eval
from enum import Enum

def rec_get(l: list, il: list[int]) -> [int, list]:
    if l == []:
        return None
    elif len(il) == 1:
        return l[il[0]]
    else:
        return rec_get(l[il.pop(0)], il)

def rec_limit(l: list, p: list[int]) -> int:
    sub_l = l.copy()
    for index in p[:-1]:
        sub_l = sub_l[index]
    return len(sub_l) - 1

def inc_pointer(p: list[int], l: list) -> list[int]:
    if p[-1] < rec_limit(l, p):
        p[-1] += 1
    else:
        p.pop()
        if p == []:
            return p
        p[-1] += 1
    return p

def compare(a: [int, list], b: [int, list], ap: list[int], bp: list[int]):
    re = Enum('re', 'null correct incorrect')
    c1 = rec_get(a, ap.copy())
    c2 = rec_get(b, bp.copy())
    # for empty lists
    if c1 == None and c2 == None:
        ap = inc_pointer(ap, a)
        if ap == []:
            return re.correct
        bp = inc_pointer(bp, b)
        if bp == []:
            return re.incorrect
        return compare(a, b, ap, bp)
    elif c1 == None:
        return re.correct
    elif c2 == None:
        return re.incorrect

    if type(c1) == type(c2) and type(c1) == int:
        if c1 < c2:
            return re.correct
        elif c1 > c2:
            return re.incorrect
        else:
            ap = inc_pointer(ap, a)
            if ap == []:
                return re.correct
            bp = inc_pointer(bp, b)
            if bp == []:
                return re.incorrect
            return compare(a, b, ap, bp)
    elif type(c1) == type(c2) and type(c1) == list:
        ap.append(0)
        bp.append(0)
        return compare(a, b, ap, bp)
    else:
        if type(c1) == list:
            ap.append(0)
            return compare(a, b, ap, bp)
        else:
            bp.append(0)
            return compare(a, b, ap, bp)

inp = open("../../input/2022/13/input", 'r').read().splitlines()[:-1]

## PART 1

pairs = [[literal_eval(inp[i]), literal_eval(inp[i+1])] for i in range(0, len(inp), 3)] # including stripping outermost brackets

right_order = [] # list of indices (!: pair indices starting at 1) if pairs in right order
pi = 1 # pair index
order_enum = Enum('order_enum', 'null correct incorrect')
for p1, p2 in pairs: # comparison
    order = compare(p1, p2, [0], [0])
    if str(p1).find('[[]') < 4 and str(p2).find('[[]') < 4:
        print(pi)
    if order == order.correct:
        right_order.append(pi)
    pi += 1

print(f"The sum of the indices of the correct pairs is {sum(right_order)}.")
