#! /usr/bin python3

def simulate(fish):
    for i in range(len(fish)):
        if fish[i]!=0:
            fish[i]-=1
        else:
            fish[i]=6
            fish.append(8)

def simulate_generation_day(fg):
    r = [fg[1], fg[2], fg[3], fg[4], fg[5], fg[6], fg[7]+fg[0], fg[8], fg[0]]
    return r

## PART 1

# input

fish = list(map(int, [l for l in open("input").readlines()][0].strip("\n").split(",")))

# simulate lantern fish

for d in range(80):
    simulate(fish)

print(f"Number of Lanternfish: {len(fish)}")

## PART 2

# simulate lanternfish for 256-80 days

fishg = [0 for i in range(9)]

for f in fish:
    fishg[f] += 1

for d in range(256-80):
   fishg = simulate_generation_day(fishg)

print(f"Number of Lanternfish: {sum(fishg)}")
   

