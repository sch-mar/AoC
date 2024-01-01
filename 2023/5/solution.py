
def get_dest(i, s): # map index, source
    for a, b, c in maps[i]:
        if s in range(b, b + c):
            return s + a - b
    return s

#inp = open('../../input/2023/5/example1', 'r').read().splitlines()[:-1]
inp = open('../../input/2023/5/input', 'r').read().splitlines()[:-1]

seeds = [int(i) for i in inp[0][7:].split()]

l = 3 # line index for input parsing
m = 0 # map index for input parsing

map_d = {0: 'seed-soil', 1: 'soil-fertilizer', 2: 'fertilizer-water', 3: 'water-light', 4: 'light-to-temperature', 5: 'temperature-humidity', 6: 'humidity-location'}
map_s = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location'] # sequence
maps = [[]]

while l < len(inp):
    if inp[l] == '':
        l += 2
        m += 1
        maps.append([])
        continue
    maps[m].append([int(i) for i in inp[l].split()])
    l += 1


seed_c = [] # seed conversion list

for seed in seeds:
    seed_c.append([seed])
    for i in range(len(maps)):
        seed_c[-1].append(get_dest(i, seed_c[-1][-1]))

print(f'Part 1: {min([l[-1] for l in seed_c])}')

############

seed_c2 = []

for i in range(0, len(seeds), 2):
    for j in range(seeds[i], seeds[i]+seeds[i+1]):
        seed_c2.append([j])
        for i in range(len(maps)):
            seed_c2[-1].append(get_dest(i, seed_c2[-1][-1]))
        if seed_c2[-1][-1] < seed_c2[0][-1]:
            print(seed_c2[-1][-1], seed_c2[0][-1], len(seed_c2))
            seed_c2.pop(0)
        elif len(seed_c2) > 1:
            seed_c2.pop(-1)
print(f'Part 2: {min([l[-1] for l in seed_c2])}')

