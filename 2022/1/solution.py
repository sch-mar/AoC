#! /usr/bin python3

inp = [l.strip("\n") for l in open("input").readlines()]

## PART 1

s = [0]
for l in inp:
    if l != '':
        s[-1] += int(l)
    else:
        s.append(0)

print(f"The elve with the most Calories is carrying {max(s)} Calories")

## PART 2

s.sort()

print(f"The 3 elves with the most carried Calories carry {sum(s[-3:])} Calories together.")


