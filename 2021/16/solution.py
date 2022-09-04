#!/usr/bin/env python3

def hexbin(hex):
    return str(bin(int(hex, base=16)))[2:]

def bindec(bin):
    return int(bin, base=2)

def decode(input):

    print(f'\nparsing: {input}')
    
    version_bin = input[:3]
    version_dec = bindec(version_bin)
    print(f'version: {version_dec} ({version_bin})')
    
    typeID_bin = input[3:6]
    typeID_dec = bindec(typeID_bin)
    print(f'type ID: {typeID_dec} ({typeID_bin})')

    if typeID_dec == 4:
        LAST_GROUP = False
        groups = 0
        nums = []
        
        while LAST_GROUP == False:
            nums.append(input[6+groups*5:11+groups*5])
            groups += 1
            if nums[-1][0] == '0':
                LAST_GROUP = True
        print(f'numbers: {nums}')
        
        ignored = input[6+groups*5:]
        print("ignored:", ignored)
        
        value_bin = "".join([i[1:] for i in nums])
        value_dec = bindec(value_bin)
        print(f'packet value: {value_dec} ({value_bin})')
    else:
        ltypeID_bin = input[6]
        ltypeID_dec = bindec(ltypeID_bin)
        print(f'length type ID: {ltypeID_dec} ({ltypeID_bin})')

        if ltypeID_bin == '0':
            totalLengthInBits_bin = input[7:20]
            totalLengthInBits_dec = bindec(totalLengthInBits_bin)
            print(f'total length in bits: {totalLengthInBits_dec} ({totalLengthInBits_bin})')

            subpackets = input[20:20+totalLengthInBits_dec]
            print("subpacket block:", subpackets)

            ignored = input[20+totalLengthInBits_dec:]
            print("ignored:", ignored)
            
            decode(subpackets)
        else:
            nSubpackets_bin = input[7:18]
            nSubpackets_dec = bindec(nSubpackets_bin)
            print(f'number of sub-packets: {nSubpackets_dec} ({nSubpackets_bin})')
            
#            for i in range(nSubpackets_dec):
            decode(
    if ignored != "":
        if int(ignored, base=2) != 0:
            decode(ignored)
    
#################################################################
    
#input = [int(i) for i in open("input").readlines()]
input = ["D2FE28", "38006F45291200", "EE00D40C823060", "8A004A801A8002F478", "620080001611562C8802118E34", "C0015000016115A2E0802F182340", "A0016C880162017C3686B18A3D4780"]

# for i in input:
#     decode(i)

example = 2
print("input:", input[example])
input[example] = hexbin(input[example])
decode(input[example])

exit()

