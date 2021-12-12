#! /usr/bin python3 

def find_all_paths1(graph, start, end, path=[]): # find all paths from s to e while visiting lowercase node only once
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node.isupper() or node not in path:
            newpaths = find_all_paths1(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def check_part2(node, path):
    #print(f"[CHECK]\tchecking path {path}: '{node}' ", end='')
    if node.isupper():
        #print(f"isupper()")
        return True
    if node not in path:
        #print(f"not in path")
        return True
    if node == 'start':
        #print(f"== 'start'")
        return False
    if node.islower() and path.count(node)<2:
        for n in set(path):
            if n != node and n.islower() and path.count(n)>1:
                #print(f"\b\b\b\b\b\b\b\b\banother cave already twice: {n, path.count(n)}times: return False")
                return False
        #print(f"== part 2")
        return True
    #print(f"\treturn False")
    return False

def find_all_paths2(graph, start, end, path=[]): # find all paths from s to e while visiting lowercase node only once
    #print(f"[NEW]\tfind all paths with g, {start}, {end}, {path}")
    path = path + [start]
    #print(f"[{start}]\tpath: {path}")
    if start == end:
        #print(f"[{start}]\tstart == end: return {[path]}\n")
        return [path]
    if start not in graph:
        #print(f"[{start}]\tstart not in graph: return None\n")
        return None
    paths = []
    #print(f"[{start}]\tfor node in {graph[start]}")
    for node in graph[start]:
        #print(f"[{start}]\tnode: {node}, path: {path}")
        if check_part2(node, path):
            newpaths = find_all_paths2(graph, node, end, path)
            for newpath in newpaths:
                #print(f"[{start}]\tpaths.append(newpath): {newpath}")
                paths.append(newpath)
        #else:
            #print(f"[{start}]\t{node} already in path or not upper")
    #print(f"[{start}]\treturn paths:")
    #for p in paths:
        #print(f"[PATH]\t{p}")
    return paths


## PART 1

# input

inp = [l.strip("\n").split("-") for l in open("input").readlines()]

# build graph

g1 = {} # graph

for l in inp:
    if l[0] not in g1:
        g1[l[0]] = []
    if l[1] != 'start':
        g1[l[0]].append(l[1])
    if l[1] not in g1:
        g1[l[1]] = []
    if l[0] != 'start':
        g1[l[1]].append(l[0])

print(f"There are {len(find_all_paths1(g1, 'start', 'end'))} paths through the cavesystem which visit small caves at most once.")

## PART 2

print(f"There are {len(find_all_paths2(g1, 'start', 'end'))} paths through the cavesystem which visit one small cave at most twice, but any other small cave at most once.")

