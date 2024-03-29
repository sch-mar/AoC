#! /usr/bin python3

def compute_input(i):
    d = [] # list of dots
    f = [] # folding instructions
    for l in i:
        if len(l)==2:
            l.reverse()
            d.append(list(map(int, l)))
        elif len(l[0])>0:
            f.append(l[0].strip("fold along ").split("="))
        #else:
            #print(f"illegal line in input: {l}")
    for l in f:
        l[1] = int(l[1])
    return d, f

def paperize(d):
    ymax = max([l[0] for l in d])
    xmax = max([l[1] for l in d])
    p = [[False for j in range(xmax+1)] for i in range(ymax+1)]
    for l in d:
        p[l[0]][l[1]] = True
    return p

def fold(p, f):
    # print(f"folding at {f[0]}={f[1]}:")
    # print_paper(p, True)
    # new side and folded(mirrored) side
    if f[0]=='y': # horizontally
        ns = [p[i] for i in range(f[1])]
        fs = [p[i] for i in range(len(p)-1, f[1], -1)]
        # combine
        yd = len(ns)-len(fs) # ydelta
        if yd>=0: # ns is longer
            for y in range(yd, f[1]):
                for x in range(len(ns[y])):
                        ns[y][x] = ns[y][x] or fs[y-yd][x]
            # print_paper(ns, True)
            return ns
        else: # fs is longer
            for y in range(abs(yd), len(p)-f[1]):
                for x in range(len(fs[y])):
                    fs[y][x] = fs[y][x] or ns[y+yd][x]
            # print_paper(fs)
            return fs                   
    else: # vertically
        ns = [[p[y][x] for x in range(f[1])] for y in range(len(p))]
        fs = [[p[y][x] for x in range(len(p[y])-1, f[1], -1)] for y in range(len(p))] # y too short by 1
        # combine
        xd = len(ns[0])-len(fs[0]) # xdelta
        if xd>=0: # nsx is longer
            for y in range(len(ns)):
                for x in range(xd, len(ns[y])):
                    ns[y][x] = ns[y][x] or fs [y][x-xd]
            # print_paper(ns, True)
            return ns
        else: # fsx is longer
            for y in range(len(fs)):
                for x in range(abs(xd), len(p[0])-f[1]):
                    fs[y][x] = fs[y][x] or ns[y][x+xd]
            # print_paper(fs, True)
            return fs
    # for y in range(min([len(ns), len(fs)])):
        # for x in range(min([len(ns[y]), len(fs[y])])):
            # ns[y][x] = ns[y][x] or fs[y][x]

def print_paper(p, dots=False):
    for l in p:
        for c in l:
            if dots==False:
                print(f"{c}\t", end ='')
            else:
                if c:
                    print("#", end='')
                else:
                    print(".", end='')
        print("")
    print("\n")
    return


## INPUT

inp = [l.strip("\n").split(",") for l in open("input").readlines()]

## PART 1

d1, f1 = compute_input(inp)
p1 = paperize(d1)

p1 = fold(p1, f1[0])
# fold(fold(p1, f1[1]), ['x',3])

print(f"After 1 fold there are {sum([sum(l) for l in p1])} dots visible.")

## PART 2

# d2, f2 = compute_input(inp)
# p2 = paperize(d2)

for i in range(1, len(f1)):
    p1 = fold(p1, f1[i])

print(f"After {len(f1)} folds the paper reads:")
print_paper(p1, True)
