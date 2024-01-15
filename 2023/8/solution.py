#########################################
# brute force approach for part 2
#
# not run succesfully, attempt aborted
# due to impatience
########################################

import re
from itertools import cycle

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
steps = 0

while [node[-1] for node in pos] != ['Z' for _ in pos]:
    i = next(ins)
    for j in range(len(pos)):
        pos[j] = nw[pos[j]][i]
    steps += 1

print(f'Part 2: {steps}')

