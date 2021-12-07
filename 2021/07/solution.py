#! /usr/bin python3

def calculate_fuel(sp, ap): # subs by position, aligning position
    fuel = 0
    for hp in range(len(sp)):
        fuel += abs(hp-ap)*sp[hp]
    return fuel

def recalculate_fuel(sp, ap): # subs by position, aligning position
    fuel = 0
    for hp in range(len(sp)):
        for i in range(abs(hp-ap)):
            fuel += sp[hp]*(i+1)
    return fuel

## PART 1

subs = list(map(int, [l for l in open("input").readlines()][0].strip("\n").split(",")))
subs.sort()

## calculate best position

sp = [0 for i in range(subs[-1]+1)] # number of subs on each position

for s in subs:
    sp[s] += 1

bp = [0, calculate_fuel(sp, 0)] # best horizontal position, fuel needed

for p in range(1, len(sp)):
    fuel = calculate_fuel(sp, p)
    if fuel<bp[1]:
        bp = [p, fuel]

print(f"The crabs need {bp[1]} fuel to align at position {bp[0]}.")

## PART 2

print("I don't understand crab engineering :(")

bp = [0, recalculate_fuel(sp, 0)]

for p in range(1, len(sp)):
    fuel = recalculate_fuel(sp, p)
    if fuel<bp[1]:
        bp = [p, fuel]

print(f"The crabs need {bp[1]} fuel to align at position {bp[0]}.")

