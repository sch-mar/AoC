#!/usr/bin/env python3

# horizontal position
hpos = 0
# depth
depth = 0

instructions = [str(s).strip("\n").split(" ") for s in open("input").readlines()]

for i in instructions:
    if i[0]=="forward":
        hpos+=int(i[1])
    elif i[0]=="down":
        depth+=int(i[1])
    elif i[0]=="up":
        depth-=int(i[1])
    else:
        print("error. can't understand instruction" + i)


print(f"hpos: {hpos}, depth: {depth}\nPuzzle answer: {hpos*depth}")

