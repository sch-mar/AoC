#! /usr/bin python3

from textwrap import wrap

def map_signals(par):
    # clean parameter into l
    sigs = []
    temp_signal = []
    for p in par:
        for e in p:
            sigs.append(e)
    for i in range(len(sigs)):
        temp_signal = wrap(sigs[i], 1)
        temp_signal.sort()
        sigs[i] = "".join(temp_signal)

    l = list(dict.fromkeys(sigs))

    len_n = {2:1, 4:4, 3:7, 7:8} # number of segments TO number
    num_s = {} # number TO segments
    r = {} # signal TO segment
    # find segments for 1,4,7,8
    for d in l:
        if len(d) in len_n:
            num_s[len_n[len(d)]] = d
    # map signal to segment
    us = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # unknown signals
    ## segment 0a
    for s in num_s[7]:
        if s in num_s[8] and s not in num_s[1] and s not in num_s[4]:
            r[s] = 'a'
            us.remove(s)
    ## segment 5f
    for s in us:
        cs = 0 # count segment
        for a in "".join(l):
            cs += int(s==a)
        if cs == 9:
            r[s] = 'f'
            us.remove(s)
            break
    ## segment 4e
    for s in us:
        cs = 0 # count segment
        for a in "".join(l):
            cs += int(s==a)
        if cs == 4:
            r[s] = 'e'
            us.remove(s)
            break
    ## segment 1b
    for s in us:
        cs = 0 # count segment
        for a in "".join(l):
            cs += int(s==a)
        if cs == 6:
            r[s] = 'b'
            us.remove(s)
            break
    ## segment 6g
    for s in us:
        cs = 0 # count segment
        for d in l:
            if len(d) in [5, 6]:
                cs += int(s in d)
        if cs == 6:
            r[s] = 'g'
            us.remove(s)
            break
    ## segment 2c
    for s in us:
        cs = 0 # count segment
        for d in l:
            cs += int(s in d)
        if cs == 8:
            r[s] = 'c'
            us.remove(s)
            break
    ## segment 3d
    r[us[0]] = 'd'
    return r

def signal_to_digit(o, m):
    segs_to_dig = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
    r = []
    for segs in o:
        decoded = [m[a] for a in segs]
        decoded.sort()
        r.append(str(segs_to_dig["".join(decoded)]))
    return int("".join(r))




## PART 1

# input

inp = [l.strip("\n").split(" | ") for l in open("input").readlines()]

for i in range(len(inp)):
    inp[i] = [inp[i][0].split(" "), inp[i][1].split(" ")]
    
c1 = 0 # counter for digits 1, 4, 7, 8

for l in inp:
    for d in l[1]:
        c1 += int(len(d) in [2, 3, 4, 7])

print(f"1, 4, 7, 8 appear {c1} times in the output values")

## PART 2

sigmap = {} # signal TO segment
outsum = 0 # sum of all outputs

for l in inp:
    ## map signals to segments
    sigmap = map_signals(l)
    outsum += signal_to_digit(l[1], sigmap)

print(f"Sum of outputs: {outsum}")


