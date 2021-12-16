#! /usr/bin python3 

from textwrap import wrap
import heapq
import sys
sys.setrecursionlimit(1000000)

def adjnodes(m, s, dia = False):
    r = []
    top = s[0]-1 >= 0
    right = s[1]+1 < len(m[0])
    bottom = s[0]+1 < len(m)
    left = s[1]-1 >= 0
    if top: r.append([s[0]-1, s[1]])
    if right: r.append([s[0], s[1]+1])
    if bottom: r.append([s[0]+1, s[1]])
    if left: r.append([s[0], s[1]-1])
    if dia:
        if top and right: r.append([s[0]-1, s[1]+1])
        if bottom and right: r.append([s[0]+1, s[1]+1])
        if bottom and left: r.append([s[0]+1, s[1]-1])
        if top and left: r.append([s[0]-1, s[1]-1])
    return r

def get_distance(q, par, ind = 1): # queue, index, paramater
    for e in q:
        if e[ind] == par:
            return e[0]
    return 0

def get_index(q, par, ind=1):
    for i in range(len(q)):
        if q[i][ind] == par:
            return i
    return None

def is_in_queue(q, par, ind=1):
    if par in [q[i][ind] for i in range(len(q))]:
        return True
    else:
        return False

def dijkstra(m, end, q, visited=[]): # map, start, end, visited = [risk, [y, x], [y2, x2]], queue
    if q == []:
        return visited[end[0]][end[1]]
    if visited == []: # initialise
        print(len(m), "x", len(m[0]))
        visited = [[False for x in range(len(m[0]))] for y in range(len(m))]
    start_d, start, origin = heapq.heappop(q)
    for ny, nx in adjnodes(m, start):
        if not visited[ny][nx]:
            if not is_in_queue(q, [ny, nx]):
                heapq.heappush(q, (start_d+m[ny][nx], [ny, nx], start))
                if start_d+m[ny][nx] < get_distance(q, [ny, nx]):
                    q[get_index(q, [ny, nx])] = (start_d+m[ny][nx], [ny, nx], start)
    visited[start[0]][start[1]] = (start_d, origin)
    return dijkstra(m, end, q, visited)
    

## INPUT

inp = [list(map(int, wrap(l.strip("\n"), 1))) for l in open("input").readlines()]

## PART 1

start = [0, 0]
end = [len(inp)-1, len(inp[0])-1]

print(dijkstra(inp.copy(), end, [(0, start, start)]))

## PART 2

inp2 = [list(map(int, wrap(l.strip("\n"), 1))) for l in open("input").readlines()]

add = [[i+j for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if i==0 and j==0:
            continue
        for y in range(len(inp)):
            if i > 0 and j==0:
                inp2.append([])
            for x in range(len(inp[0])):
                y2 = y + len(inp)*i
                x2 = x + len(inp[0])*j
                v = inp2[y][x]+add[i][j]
                if v > 9:
                    v -= 9
                inp2[y2].append(v)

start = [0, 0]
end = [len(inp2)-1, len(inp2[0])-1]
print(dijkstra(inp2.copy(), end, [(0, start, start)]))

