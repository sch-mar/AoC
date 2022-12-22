#! /usr/bin python3

import re
from copy import deepcopy

def shorten(s: str) -> str:
    return s[0]

def dijkstra(graph, start, duration):
    for tunnel in graph[start]['tunnels']:
        pass

reg = re.compile("\d+|[A-Z]{2}")
inp = [re.findall(reg, l) for l in open("../../input/2022/16/example", 'r').read().splitlines()[:-1]]

graph = {l[0]: {'rate': int(l[1]), 'tunnels': l[2:]}for l in inp}

## PART 2

duration = 26
q = [{'AAAA': {'open': [], 'released': 0}}]
paths = {}

while q:
    cont = False

    # queue length
    if len(q) % 1000 == 0:
        print(len(q))
    
    # path, values, locations
    p, v = list(q.pop(0).items())[0]
    loc1 = p[-4:-2]
    loc2 = p[-2:]

    # increase released pressure
    for valve in v['open']:
        v['released'] += graph[valve]['rate']

    # forget path
    if [p[i:i+4] for i in range(0, len(p), 4)].count(loc1 + loc2) > 4 or len(set([p[i:i+4] for i in range(0, len(p), 4)])) / (len(p) / 4) < 0.72: # 0.45 for example
        continue

    # open valve if not opened, but check neighbouring valve sizes first
    if loc1 not in v['open'] and graph[loc1]['rate'] > 0 and max([graph[adj]['rate'] for adj in graph[loc1]['tunnels'] if adj not in v['open']], default=0) <= graph[loc1]['rate']:
        v['open'].append(loc1)
        cont = True
    if loc2 not in v['open'] and graph[loc2]['rate'] > 0 and max([graph[adj]['rate'] for adj in graph[loc2]['tunnels'] if adj not in v['open']], default=0) <= graph[loc2]['rate']:
        v['open'].append(loc2)
        cont = True
    if cont:
        q.append({p + loc1 + loc2: deepcopy(v)})
        continue
    
    # if maximum length or all valves are open
    if len(p) / 4 == duration or len(v['open']) == len([g for g in graph if graph[g]['rate']]):
        paths[p] = v['released']#{p: v})
        continue

    # move
    for adj in graph[loc1]['tunnels']:
        q.append({p + adj: deepcopy(v)})




## PART 1

# max_pressure = dijkstra(graph, 'A', 30)

duration = 30
q = [{'AA': {'open': [], 'released': 0}}] # released 0 for Part 1, released 1 for example
paths = {}

while q:
    if len(q) % 1000 == 0:
        print(len(q))
    p, v = list(q.pop(0).items())[0] # path, values
    loc = p[-2:]
    # test for circular movement (redundant because circular movement doesn't improve path weight)
    # if max({p.count(valve) for valve in p}) > 3:
    #     continue
    # increase released pressure
    for valve in v['open']:
        v['released'] += graph[valve]['rate']
    # if all valves open
    # forget path if to narrow
    # if len(p) > duration and len(v['open'])/len(p)/2 < 0.05:
    # if len(p) / 2 >= duration and len(set([p[i]+p[i+1] for i in range(0, len(p), 2)])) / (len(p) / 2) < len(graph) / duration:
    # if len(p) > duration and len(v['open']) / len(p) / 2 < len(graph) / duration:
    # if len(set([p[i]+p[i+1] for i in range(0, len(p), 2)])) / (len(p) / 2) < len(graph) / duration:
    # if [p[i]+p[i+1] for i in range(0, len(p), 2)].count(loc) > (len(p) / 2) / (len(v['open']) + 1):
    # forget path if loc visited too often or 
    if [p[i]+p[i+1] for i in range(0, len(p), 2)].count(loc) > 4 or len(set([p[i]+p[i+1] for i in range(0, len(p), 2)])) / (len(p) / 2) < 0.72: # 0.45 for example
        continue
    # open valve if not opened, but check neighbouring valve sizes first
    if loc not in v['open'] and graph[loc]['rate'] > 0 and max([graph[adj]['rate'] for adj in graph[loc]['tunnels'] if adj not in v['open']], default=0) <= graph[loc]['rate']:
        v['open'].append(loc)
        q.append({p + loc: deepcopy(v)})
        continue
    # maximum length or all valves are open
    if len(p) == duration * 2 or len(v['open']) == len([g for g in graph if graph[g]['rate']]):
        paths[p] = v['released']#{p: v})
        continue
    for adj in graph[loc]['tunnels']:
        q.append({p + adj: deepcopy(v)})

# finish pressure release
for path in paths:
    for rate in [graph[g]['rate'] for g in graph if graph[g]['rate']]:
            paths[path] += rate * (duration - len(path) / 2)

for path, released in sorted(paths.items(), key=lambda item: item[1], reverse=True)[:20]:
    print('-'.join([path[i]+path[i+1] for i in range(0, len(path), 2)]), released)
print(len(paths))

