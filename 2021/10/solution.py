#! /usr/bin python3

def check_line(l): # returns 0(good) or 1(incomplete) or 2(corrupted), first illegal character or completion sequence
    b = {'(':')', '[':']', '{':'}', '<':'>'} # chunk borders
    chs = [] # chunks
    for c in l:
        # if open: chs.append
        if c in b:
            chs.append(b[c])
        else:
            if c == chs[-1]:
                chs.pop(-1)
            else:
                return 2, c
    if len(chs)>0:
        chs.reverse()
        return 1, "".join(chs)
    else:
        return 0, ''

def calculate2(cs): # closing sequence
    s = 0 # sum
    p = {')':1, ']':2, '}':3, '>':4}
    for c in cs:
        s *= 5
        s += p[c]
    return s

from textwrap import wrap
import math

## PART 1

inp = [wrap(l.strip("\n"), 1) for l in open("input").readlines()]
s1 = 0 #sum
p1 = {')':3, ']':57, '}':1197, '>':25137}
lResult = []

for l in inp:
    lResult = check_line(l)
    if lResult[0]==2:
        s1 += p1[lResult[1]]

print(f"The total syntax error score is {s1}.")

## PART 2
s2 = []

for l in inp:
    lResult = check_line(l)
    if lResult[0]==1:
        s2.append(calculate2(lResult[1]))

s2.sort()

print(f"The middle autocomplete score is {s2[math.floor(len(s2)/2)]}.")



