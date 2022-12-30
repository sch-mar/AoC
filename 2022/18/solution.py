#! /usr/bin python3

class Cube:
    def __init__(self, coord: list[int]):
        self.coord = tuple(map(int, coord))
        self.x, self.y, self.z = self.coord
        self.sides = []
        # calculate sides
        for x,y,z in {(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)}:
            self.sides.append((
                    frozenset({self.x, self.x + x}),
                    frozenset({self.y, self.y + y}),
                    frozenset({self.z, self.z + z})
                    ))

    def __str__(self):
        return f"Cube at {self.coord}\t{self.sides}"

    def __eq__(self, other):
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)

    def adjacent_coord(self):
        return list(map(lambda i: [e for e in i][0], [set(zip(list(side[0])*2, list(side[1]) * 2, list(side[2]) * 2)) - {self.coord} for side in self.sides]))

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

# cuboid
## find min/max for x,y,z
cubecoords = [cube.coord for cube in cubes]
xl, yl, zl = (l + 1 for l in map(max, zip(*cubecoords)))
xs, ys, zs = (s - 1 for s in map(min, zip(*cubecoords)))

## BFS
q = [(xs, ys, zs)]
visited = set()
while q:
    p = q.pop(0) # position
    for x,y,z in Cube(p).adjacent_coord():
        # if adj in boundaries and not part of droplet and not yet visited
        if xs <= x <= xl and ys <= y <= yl and zs <= z <= zl and (x,y,z) not in visited and Cube((x,y,z)) not in cubes:
            visited.add((x,y,z))
            q.append((x,y,z))

visited_sides = set()
for v in visited:
    for side in Cube(v).sides:
        visited_sides.add(side)

print("Part 2:", len(set(exposed_sides) & visited_sides))

