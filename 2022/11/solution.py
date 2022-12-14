#! /usr/bin python3

import math
import gmpy2

def my_eval(op, old):
    # value 1
    if op[0] == "old":
        v1 = old
    else:
        v1 = int(op[0])
    # value 2
    if op[2] == "old":
        v2 = old
    else: v2 = int(op[2])
    # operation
    if op[1] == '+':
        return v1 + v2
    elif op[1] == '-':
        return v1 - v2
    elif op[1] == '*':
        return v1 * v2
    elif op[1] == '/':
        return v1 / v2
    else:
        raise ValueError

inp = [l.strip() for l in open("../../input/2022/11/example", 'r').read().splitlines()[:-1]]

monkeys = {}
monkey = '0'
for l in inp:
    l = l.split(':')
    if "Monkey" in l[0]:
        monkeys[l[0][-1]] = {"items_inspected": 0}
        monkey = l[0][-1]
    elif l[0] == "Starting items":
        monkeys[monkey]["items"] = list(map(int, l[1].split(',')))
    elif l[0] == "Operation":
        monkeys[monkey]["op"] = l[1].split()[2:]
    elif l[0] == "Test":
        monkeys[monkey]["test"] = int(l[1].split()[-1])
    elif "If" in l[0]:
        if l[0].split()[1] == "true":
            monkeys[monkey]["true"] = l[1][-1]
        else:
            monkeys[monkey]["false"] = l[1][-1]

## PART 1
for r in range(20): # 20 rounds
    for monkey in monkeys.values():
        while monkey["items"]:
            item = my_eval(monkey["op"], monkey["items"].pop(0))
            item = math.floor(item / 3)
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)
            monkey["items_inspected"] += 1

print(f"The level of monkey business is {math.prod(sorted([monkey['items_inspected'] for monkey in monkeys.values()])[-2:])}.")

## PART 2
inp = [l.strip() for l in open("../../input/2022/11/input", 'r').read().splitlines()[:-1]]

monkeys = {}
monkey = '0'
for l in inp:
    l = l.split(':')
    if "Monkey" in l[0]:
        monkeys[l[0][-1]] = {"items_inspected": 0}
        monkey = l[0][-1]
    elif l[0] == "Starting items":
        monkeys[monkey]["items"] = list(map(int, l[1].split(',')))
    elif l[0] == "Operation":
        monkeys[monkey]["op"] = l[1].split()[2:]
    elif l[0] == "Test":
        monkeys[monkey]["test"] = int(l[1].split()[-1])
    elif "If" in l[0]:
        if l[0].split()[1] == "true":
            monkeys[monkey]["true"] = l[1][-1]
        else:
            monkeys[monkey]["false"] = l[1][-1]

# manage big numbers (credit: [Jonathan Paulson](https://www.youtube.com/watch?v=W9vVJ8gDxj4))
lcm = 1
for x in [monkey['test'] for monkey in monkeys.values()]:
    lcm = lcm*x#//math.gcd(lcm, x)

for r in range(10000): # 10000 rounds
    for monkey in monkeys.values():
        while monkey["items"]:
            item = my_eval(monkey["op"], monkey["items"].pop(0))
            item %= lcm
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)
            monkey["items_inspected"] += 1

print(f"The level of monkey business is {math.prod(sorted([monkey['items_inspected'] for monkey in monkeys.values()])[-2:])}.")

