import math

inp = open('../../input/2023/4/input', 'r').read().splitlines()[:-1]

points = 0
have = []
win = []
points = []

for line in inp:
    line = [a.split() for a in line[10:].split('|')] # 8: for example, 10: for input
    have.append([int(a) for a in line[0]])
    win.append([int(a) for a in line[1]])
    points.append(math.floor(pow(2, len(set(win[-1])&set(have[-1]))-1)))

print(f'Part 1: {sum(points)}')

########

matches = []

for i in range(len(have)):
    matches.append(len(set(win[i])&set(have[i])))

scratchcards = {i: 1 for i in range(len(inp))}
q = [i for i in range(len(inp))]
part2 = len(inp)

while q:
    for i in range(matches[q[0]]):
        scratchcards[q[0]+i+1] += scratchcards[q[0]]
        part2 += scratchcards[q[0]]
    q.pop(0)

print(f'Part 2: {part2}')

