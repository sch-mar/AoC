#! /usr/bin python3

class Cube:
    def __init__(self, coord: list[int]):
        self.coord = tuple(map(int, coord))
        self.x, self.y, self.z = self.coord
        self.sides = []
        # calculate sides
        for x,y,z in {(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)}:
            self.sides.append((
                    {self.x, self.x + x},
                    {self.y, self.y + y},
                    {self.z, self.z + z}
                    ))

    def __str__(self):
        return f"Cube at {self.coord}\t{self.sides}"

    def __eq__(self, other):
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)

inp = open("../../input/2022/18/input", 'r').read().splitlines()[:-1]

cubes = [Cube(l.split(',')) for l in inp]

exposed_sides = []

for cube in cubes:
    for side in cube.sides:
        if side not in exposed_sides:
            exposed_sides.append(side)
        else:
            exposed_sides.remove(side)

print("Part 1:", len(exposed_sides))

# for each exposed side
enclosed_cubes = set()
for side in exposed_sides:
    # try to build both possible cubes out of exposed sides
    for center in zip(list(side[0]) * 2, list(side[1]) * 2, list(side[2]) * 2):
        c = Cube(center)
        miss = False
        for s in c.sides:
            if s not in exposed_sides:
                miss = True
                break
        if not miss and c not in cubes:
            enclosed_cubes.add(c)

print(len(enclosed_cubes))

for cube in enclosed_cubes:
    for side in cube.sides:
        if side in exposed_sides:
            exposed_sides.remove(side)

print("Part 2:", len(exposed_sides))


