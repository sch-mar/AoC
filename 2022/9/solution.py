#! /usr/bin python3

def follow(k1, k2): # k2 follows k1
    dx = k1[0] - k2[0]
    dy = k1[1] - k2[1]
    if abs(dx) >= 2 or abs(dy) >= 2:
        if abs(dx) == 1 or abs(dy) == 1 or (abs(dx) == 2 and abs(dy) == 2): # diagonal
            #print("moving diagonal")
            k2[0] += int(dx / abs(dx))
            k2[1] += int(dy / abs(dy))
        else: # horizontal/vertical
            if dx != 0:
                #print("moving horizontal")
                k2[0] += int(dx / abs(dx))
            else:
                #print("moving vertical")
                k2[1] += int(dy / abs(dy))
    return k2

def visited(l, inp): # length of rope >=2, inp
    rope = [[0, 0] for n in range(l)] # Head .. Tail
    direction_converter = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
    visited = {(0, 0)}
    for l in inp:
        direction = direction_converter.get(l[0])
        distance = int(l[1])
        #print("direction", l[0], direction, "distance", distance)
        for i in range(distance):
            #print(".step #", i)
            rope[0][0] += direction[0]
            rope[0][1] += direction[1]
            for k in range(1, len(rope)): # knots starting with second (head+1) as k=1
                rope[k] = follow(rope[k-1], rope[k])
                #print("...rope", " ; ".join([str(k[0]) + "," + str(k[1]) for k in rope]))
            visited.add((rope[-1][0], rope[-1][1]))
        #print("rope", rope)
        #print(";".join([str(k[0]) + ", " + str(k[1]) for k in rope]))
        #print(sorted(visited))
            #wait = input()
    #print(sorted(visited))
    return visited

inp = [l.split() for l in open("input", 'r').read().splitlines()][:-1]

## PART 1

print(f"The rope tail visited {len(visited(2, inp))} positions at least once.")

## PART 2

print(f"The tail of the longer rope visited {len(visited(10, inp))} positions at least once.")


