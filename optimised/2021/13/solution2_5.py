#! /usr/bin python3

def compute_input2_5(i):
    print("computing input")
    d = [0, 0, []] # ysize, xsize, list of coordinates
    f = [] # folding instructions
    for l in i:
        if len(l)==2:
            l.reverse()
            d[2].append(list(map(int, l)))
            if d[2][-1][0]>d[0]:
                d[0] = d[2][-1][0]
            if d[2][-1][1]>d[1]:
                d[1] = d[2][-1][1]
        elif len(l[0])>0:
            f.append(l[0].strip("fold along ").split("="))
        #else:
            #print(f"illegal line in input2_5: {l}")
    d[0] += 1
    d[1] += 1
    for l in f:
        l[1] = int(l[1])
    return d, f

def fold2_5(d, f): # using coordinates instead of matrix
    print(f"folding at {f[0]}={f[1]}: ({d[0]}x{d[1]})")
    if f[0] == 'y': # horizontally
        d[0] = f[1]
        # print(f"new size: {d[0]}x{d[1]}")
        i = 0
        while i < len(d[2]):
            # print(f"{d[2][i][0]} ({f[1]})")
            if d[2][i][0] > f[1]:
                if [d[2][i][0]-f[1], d[2][i][1]] not in d[2]:
                    # print(d[2][i][0]-2*(d[2][i][0]-f[1]) >= f[1])
                    d[2].append([f[1]-(d[2][i][0]-f[1]), d[2][i][1]])
                # print(f"popping {d[2][i]}")
                d[2].pop(i)
            elif d[2][i][0] == f[1]:
                d[2].pop(i)
            else:
                # print(f"not popping {d[2][i]}")
                i += 1
    else: # horizontally
        d[1] = f[1]
        # print(f"new size: {d[0]}x{d[1]}")
        i = 0
        while i < len(d[2]):
            if d[2][i][1] > f[1]:
                if [d[2][i][0], d[2][i][1]-2*(d[2][i][1]-f[1])] not in d[2]:
                    # print(d[2][i][1]-2*(d[2][i][1]-f[1]) == f[1]-(d[2][i][1]-f[1]))
                    d[2].append([d[2][i][0], f[1]-(d[2][i][1]-f[1])])
                d[2].pop(i)
            elif d[2][i][1] == f[1]:
                d[2].pop(i)
            else:
                i += 1
                if (len(d[2])-i)%10000 == 0:
                    print(len(d[2])-i)
    # print_paper2_5(d)
    return d

def print_paper2_5(d):
    print(f"printing paper: {d[0]}x{d[1]}")
    p = [['.' for x in range(d[1])] for y in range(d[0])]
    for l in d[2]:
        # print(l)
        p[l[0]][l[1]] = '#'
    for l in p:
        for c in l:
            print(c, end='')
        print('')
    return

## INPUT

print("starting")

inp = [l.strip("\n").split(",") for l in open("input2_5").readlines()]

print(f"input length: {len(inp)}")

## PART 1

print("part 1")

d1, f1 = compute_input2_5(inp)

d1 = fold2_5(d1, f1[0])

# print(f"After 1 fold there are {sum([sum(l) for l in p1])} dots visible.")

## PART 2

# d2, f2 = compute_input2_5(inp)
# p2 = paperize(d2)

for i in range(1, len(f1)):
    d1 = fold2_5(d1, f1[i])

print(f"After {len(f1)} folds the paper reads:")
print_paper2_5(d1)
