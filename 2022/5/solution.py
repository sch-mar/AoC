#! /usr/bin python3

inp = open("input", "r").read().splitlines()[:-1]

## PART 1

p1 = [list(reversed(list(filter(None, x)))) for x in zip(*[[s[n:n+4].strip(' []') for n in range(0, len(s), 4)] for s in [l for l in inp[:inp.index('') -1]]])]
p2 = [list(reversed(list(filter(None, x)))) for x in zip(*[[s[n:n+4].strip(' []') for n in range(0, len(s), 4)] for s in [l for l in inp[:inp.index('') -1]]])]
moves = [list(map(int, l.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split())) for l in inp[inp.index('') +1:]]

for m in moves:
    for i in range(m[0]):
        p1[m[2]-1].append(p1[m[1]-1].pop())

print(f"The crates {''.join([s[-1] for s in p1])} end up on top of the stacks")

## PART 2

for m in moves:
    p2[m[2]-1] += (p2[m[1]-1][-m[0]:])
    p2[m[1]-1] = p2[m[1]-1][:-m[0]]

print(f"The crates {''.join([s[-1] for s in p2])} end up on top of the stacks")

