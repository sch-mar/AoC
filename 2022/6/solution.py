#! /usr/bin python3

inp = open("input", 'r').readlines()[0]

## PART 1

p1 = 4
for i in range(len(inp)):
    if sorted(inp[i:i+4]) == sorted(set(inp[i:i+4])):
        print(f"The first start-of-packet marker is detected after processing {p1} characters.")
        break
    p1 += 1

## PART 2

p2 = 14
for i in range(len(inp)):
    if sorted(inp[i:i+14]) == sorted(set(inp[i:i+14])):
        print(f"The first start-of-message marker is detected after processing {p2} characters.")
        break
    p2 += 1


