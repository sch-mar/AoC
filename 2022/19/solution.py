#! /usr/bin python3

import re

class Blueprint:
    def __init__(self, s: str, id: int):
        self.ID = str(id)
        s = re.findall(r'\d+', s)
        self.ore = [(s[1], 'ore')]
        self.clay = [(s[2], 'ore')]
        self.obs = [(s[3], 'ore'), (s[4], 'clay')]
        self.geo = [(s[5], 'ore'), (s[6], 'obsidian')]

    def __str__(self):
        return self.ID

class Robot:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Resource:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


inp = open("../../input/2022/19/example", 'r').read().splitlines()[:-1]

blueprints = [Blueprint(l, i) for i, l in enumerate(inp, 1)]

for l in blueprints:
    print(l)

