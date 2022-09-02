#!/usr/bin/env python3

def hexbin(hex):
    return str(bin(int(hex, base=16)))[2:]

#input = [int(i) for i in open("input").readlines()]
input = "D2FE28"

packet1 = input

# hexbin conversion: bin = str(bin(int(hex, base=16)))[2:]

packet1_bin = hexbin(packet1)
version_bin = packet1_bin[:3]
version_dec = int(version_bin, base=2)

print(f'version: {version_dec} ({version_bin})')

