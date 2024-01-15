import re
from itertools import cycle
import math

#inp = open('../../input/2023/8/example1', 'r').read().splitlines()[:-1]
#inp = open('../../input/2023/8/example2', 'r').read().splitlines()[:-1]
#inp = open('../../input/2023/8/example3', 'r').read().splitlines()[:-1]
inp = open('../../input/2023/8/input', 'r').read().splitlines()[:-1]

ins = cycle([{'R': 1, 'L': 0}[a] for a in inp[0]])
nw = {a: [b, c] for a,b,c in [re.findall(r'\w+', line) for line in inp[2:]]}

pos = 'AAA'
steps = 0

while pos != 'ZZZ':
    pos = nw[pos][next(ins)]
    steps += 1

print(f'Part 1: {steps}')

#---

ins = cycle([{'R': 1, 'L': 0}[a] for a in inp[0]])

pos = [node for node in nw.keys() if node[-1] == 'A']
steps = [0 for _ in pos]
steps2 = [[] for _ in pos]
ins2 = [cycle([{'R': 1, 'L': 0}[a] for a in inp[0]]) for _ in pos]

for i in range(len(pos)):
    while len(steps2[i]) < 20:
        while pos[i][-1] != 'Z':
            pos[i] = nw[pos[i]][next(ins2[i])]
            steps[i] += 1
        steps2[i].append(steps[i])
        pos[i] = nw[pos[i]][next(ins2[i])]
        steps[i] += 1

diffs = []
for s in steps2:
    diffs.append([s[i+1]-s[i] for i in range(len(s)-1)])
avgs = [sum(d)/len(d) for d in diffs]
avgs = [int(a) for a in avgs]

#while [node[-1] for node in pos] != ['Z' for _ in pos]:
#    i = next(ins)
#    for j in range(len(pos)):
#        pos[j] = nw[pos[j]][i]
#    steps += 1

print(f'Part 2: {math.lcm(*avgs)}')

