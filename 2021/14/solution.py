#! /usr/bin python3 

from textwrap import wrap
import math
import time

def compute_inp(i):
    pt = []
    pir = {}
    for l in i:
        if len(l)==2: # pir
            pir[l[0]] = l[1]
        elif l[0]!='':
            pt = wrap(l[0], 1)
            print(pt)
    return pt, pir

def insert_polymers(pt, pir, cs=100000):
    if len(pt)<cs:
        r = [pt[0]]
        for ps in [pt[i]+pt[i+1] for i in range(len(pt)-1)]:
            r.append(pir[ps])
            r.append(ps[1])
    else:
        # !!! t = wrap(pt, math.ceil(len(pt)/math.ceil(len(pt)/cs)))
        t = [pt[i:i+math.ceil(len(pt)/cs)] for i in range(0, len(pt), math.ceil(len(pt)/cs))]
        for i in range(len(t)):
            t[i] = insert_polymers(t[i], pir)
        r = t[0]
        for i in range(1, len(t)):
            r.append(pir[t[i-1][-1]+t[i][0]])
            for e in t[i]:
                r.append(e)                
    return r
        
def compute_inp2(i):
    pt_ = []
    pt = []
    pir = {}
    for l in i:
        if len(l)==2: # pir
            pir[l[0]] = l[1]
        elif l[0]!='':
            pt_ = wrap(l[0], 1)
            for j in range(len(pt_)-1):
                pt.append(pt_[j]+pt_[j+1])
    return pt, pir

def insert_polymers2(pts, pir):
    r = pts.copy()
    for key in pts:
        if pts[key]>0:
            r[key] -= pts[key]
            r[key[0]+pir[key]] += pts[key]
            r[pir[key]+key[1]] += pts[key]
    return r

def count2(pts):
    chars = list(set("".join([key for key in pts])))
    counter = {}
    for c in chars:
        counter[c] = 0
    for key in pts:
        counter[key[0]] += pts[key]
        counter[key[1]] += pts[key]
    min = float('inf')
    max = 0
    for key in counter:
        counter[key] = math.ceil(counter[key]/2)
        if counter[key]>max:
            max = counter[key]
        if counter[key]<min:
            min = counter[key]
    return max - min



## INPUT

inp = [l.strip("\n").split(" -> ") for l in open("input").readlines()]

## PART 1

pt1, pir1 = compute_inp(inp)

for i in range(10):
    pt1 = insert_polymers(pt1, pir1)

pt1_summary = [pt1.count(p) for p in set(pt1)]

print(f"Solution Part 1: {max(pt1_summary) - min(pt1_summary)}")

## PART 2


pt2, pir2 = compute_inp2(inp)
pt2s = {}

for k in pir2:
    pt2s[k]=0

for e in pt2:
    pt2s[e] += 1

for i in range(40):
    pt2s = insert_polymers2(pt2s, pir2)

print(f"Solution Part 2: {count2(pt2s)}")

