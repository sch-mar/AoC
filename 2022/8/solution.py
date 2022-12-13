#! /usr/bin python3

def viewing_distance(grid, r, c, right, down):
    d = len(grid[0])
    grid = [int(tree) for row in grid for tree in row]
    vd = 0
    h1 = grid[c + r * d]
    h2 = -1
    while h2 < h1 and r != 0 and c != 0 and r != d - 1 and c != len(grid)/d - 1:
        vd += 1
        c += right
        r += down
        h2 = grid[c + r * d]
    return vd


inp = [list(l) for l in open("input", "r").read().splitlines()[:-1]]

## PART 1

p1 = len(inp) * 2 + (len(inp[0]) - 2) * 2
for r in range(1, len(inp[0])-1):
    for c in range(1, len(inp)-1):
        h = inp[r][c] # current height
        left = not bool([inp[r][i] for i in range(c) if inp[r][i] >= h])
        top = not bool([inp[i][c] for i in range(r) if inp[i][c] >= h])
        right = not bool([inp[r][i] for i in range(c+1, len(inp[r])) if inp[r][i] >= h])
        bottom = not bool([inp[i][c] for i in range(r+1, len(inp)) if inp[i][c] >= h])
        p1 += int(left or top or right or bottom)

print(f"{p1} Trees are visible form outside the grid.")

## PART 2

p2 = set([]) # scenic scores (1 dimension)
for r in range(1, len(inp[0])-1):
    for c in range(1, len(inp)-1):
        h = inp[r][c] # current height
        left = viewing_distance(inp.copy(), r, c, -1, 0)
        top = viewing_distance(inp.copy(), r, c, 0, -1)
        right = viewing_distance(inp.copy(), r, c, 1, 0)
        bottom = viewing_distance(inp.copy(), r, c, 0, 1)
        p2.add(left * top * right * bottom)

print(f"The highest scenic score possible is {max(p2)}.")

