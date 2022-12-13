#! /usr/bin python3

inp = [l.split() for l in open("input", 'r').read().splitlines()[:-1]]

## PART 1

X = [1] # register value at end of cycle = index
for l in inp:
    X.append(X[-1])
    if l[0] == 'addx':
        X.append(X[-1] + int(l[1]))

signal_strengths = []

for i in range(20, len(X), 40):
    signal_strengths.append(i*X[i-1])

print(f"The sum of the signal strengths is {sum(signal_strengths)}.")

## PART 2

screen = []
for l in range(6): # line
    screen.append([])
    for p in range(40): # position (horizontal)
        if p in [X[p+40*l], X[p+40*l]+1, X[p+40*l]-1]:
            screen[-1].append('#')
        else:
            screen[-1].append('.')

#print(["".join(l) for l in screen])
print('\n'.join(["".join(l) for l in screen]))

