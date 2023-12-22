import re

class Game:
    def __init__(self, line):
        self.game_id = 1
        self.handfuls = [a.split(',') for a in line.split(':')[1].split(';')]

    def __str__(self):
        return f'{self.game_id}: {self.handfuls}'


#inp = open('../../input/2023/2/example1', 'r').read().splitlines()
inp = open('../../input/2023/2/input', 'r').read().splitlines()


max_cubes = {'red': 12, 'green': 13, 'blue': 14}
part1 = sum(list(range(1, len(inp))))

for index, line in enumerate(inp):
    line =  [a.split(' ') for a in re.findall(r'\d+\s\w+', line)]
    for a in line:
        if int(a[0]) > max_cubes[a[1]]:
            part1 -= index + 1
            break

print(f'Part 1: {part1}')

#########

part2 = 0

for index, line in enumerate(inp):
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}
    line = [a.split(' ') for a in re.findall(r'\d+\s\w+', line)]
    for a in line:
        if int(a[0]) > max_cubes[a[1]]:
            max_cubes[a[1]] = int(a[0])
    part2 += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

print(f'Part 2: {part2}')



