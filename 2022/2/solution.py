#! usr/bin python3

def points(r):
    dict = {'A': 1, 'B': 2, 'C': 3}
    r = ''.join(r)
    if r[0] == r[1]:
        return 3 + dict[r[1]]
    elif r in ['AB', 'BC', 'CA']:
        return 6 + dict[r[1]]
    else:
        return dict[r[1]]

def choose(r):
    dict = {'X': {'A': 'C', 'B': 'A', 'C': 'B'}, 'Y': {'A': 'A', 'B': 'B', 'C': 'C'}, 'Z': {'A': 'B', 'B': 'C', 'C': 'A'}}
    return [r[0], dict[r[1]][r[0]]]

inp = [l.strip("\n").split(' ') for l in open("input", "r").readlines()][:-1]

## PART 1
dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}
s = 0 #score
for r in inp: # rounds
    s += points([r[0], dict[r[1]]])

print(f"According to my strategy guide I would get a total score of {s} points.")
   
## PART 2

s = 0
for r in inp:
    s += points(choose(r))

print(f"According to my strategy guide I would get a total score of {s} points.")   

