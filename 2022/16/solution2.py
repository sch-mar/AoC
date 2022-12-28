"""
with help from Jonathan Paulson
https://youtu.be/DgqkVDr1WX8
and translation inspiration by u/LXXIII7373
https://www.reddit.com/r/adventofcode/comments/zwvmz9/2022_day_16_part_2python_my_solution_gives_an/
"""

import re
from copy import deepcopy

reg = re.compile("\d+|[A-Z]{2}")
inp = [re.findall(reg, l) for l in open("../../input/2022/16/input", 'r').read().splitlines()[:-1]]

graph = {}
rates = {}

for i in inp:
    graph[i[0]] = i[2:]
    rates[i[0]] = int(i[1])

def main():
    DP = {} # Dynamic Programming Map

    # starting position, opened valves, time left, workers
    def f(position: str, opened: list[str], time: int, otherWorkers: int):
        nonlocal DP
        if not time:
            return f('AA', opened, 26, otherWorkers - 1) if otherWorkers else 0

        # How many states are there?
        #  2**15 subsets of opened valves
        #  50 possible positions
        #  27 possible time values [0-30]/[0-26]
        #  2 possible worker values 1/2
        # => ~ 88_000_000
        key = (position, tuple(sorted(opened)), time, otherWorkers)
        if key in DP:
            return DP[key]
        
        ans = 0
        # open valve
        if position not in opened and rates[position] > 0:
            opened.add(position)
            ans = max(ans, rates[position] * (time - 1) + f(position, opened, time - 1, otherWorkers))
            opened.remove(position)
        # take tunnel
        for adj in graph[position]:
            ans = max(ans, f(adj, opened, time - 1, otherWorkers))

        DP[key] = ans
        return ans

    # print(f"Part 1: {f('AA', set(), 30, 0)}")
    print(f"Part 2: {f('AA', set(), 26, 1)}")

main()
