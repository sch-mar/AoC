#! /usr/bin python3

import math

def hexbin(hex):
    return str(bin(int('1'+hex, base=16)))[3:]

def binhex(bin):
    return str(hex(int(bin, base=2)))[2:]

def bindec(bin):
    return int(bin, base=2)

#######

class Packet:
    def __init__(self, hex: str = None, bin: str = None):
        # init = 'hex' if hex else 'bin'
        # print("new packet", init)
        # input()
        self.hex = hex if hex else binhex(bin)
        self.bin = bin if bin else hexbin(hex)
        p = 0
        # packet version
        self.version = bindec(self.bin[:p+3])
        p += 3
        # packet type ID
        self.typeID = bindec(self.bin[p:p+3])
        p += 3
        self.type = 'lit' if self.typeID == 4 else 'op'
        if self.type == 'lit':
            # literal packet
            self.value = ''
            while True:
                group = self.bin[p:p+5]
                self.value += group[1:]
                p += 5
                if group[0] == '0':
                    break
            self.value = bindec(self.value)
        else:
            # operator packet
            self.lengthID = self.bin[p]
            p += 1
            if self.lengthID == '0':
                self.sub_length = bindec(self.bin[p:p+15])
                p += 15
                sub_end = p + self.sub_length
                # sub packets
                self.sub_packet_bin = self.bin[p:p+self.sub_length]
                self.sub_packets = []
                while True:
                    self.sub_packets.append(Packet(bin=self.bin[p:]))
                    p += self.sub_packets[-1].p
                    if p == sub_end:
                        break
            else:
                self.sub_count = bindec(self.bin[p:p+11])
                p += 11
                # sub_packets
                self.sub_packets = []
                for _ in range(self.sub_count):
                    self.sub_packets.append(Packet(bin=self.bin[p:]))
                    p += self.sub_packets[-1].p
            # packet value
            match self.typeID:
                case 0:
                    self.type += '_sum'
                    self.value = sum([packet.value for packet in self.sub_packets])
                case 1:
                    self.type += '_prod'
                    self.value = math.prod([packet.value for packet in self.sub_packets])
                case 2:
                    self.type += '_min'
                    self.value = min([packet.value for packet in self.sub_packets])
                case 3:
                    self.type += '_max'
                    self.value = max([packet.value for packet in self.sub_packets])
                case 5:
                    self.type += '_gt'
                    self.value = 1 if self.sub_packets[0].value > self.sub_packets[1].value else 0
                case 6:
                    self.type += '_lt'
                    self.value = 1 if self.sub_packets[0].value < self.sub_packets[1].value else 0
                case 7:
                    self.type += '_eq'
                    self.value = 1 if self.sub_packets[0].value == self.sub_packets[1].value else 0
        # terminal pointer
        self.p = p

    def __str__(self):
        s = f"v:{self.version},t:{self.type}"
        if self.type == 'lit':
            s += f",value:{self.value}"
        else:
            s += f",i:{self.lengthID}"
            if self.lengthID == '0':
                s += f",l:{self.sub_length},c:{len(self.sub_packets)}"
            else:
                s += f",c:{self.sub_count}"
        s += f",p:{self.p}"
        return s

    def print_hex(self):
        print(self.hex)
    
    def print_bin(self):
        print(self.bin)

    def print(self):
        print(self)
        # check for inner packets
        if self.type == 'op':
            for packet in self.sub_packets:
                packet.print()

    def version_sum(self):
        vs = self.version
        if self.type == 'op':
            for packet in self.sub_packets:
                vs += packet.version_sum()
        return vs



# example = 'D2FE28'
# example = '38006F45291200'
# example = 'EE00D40C823060'
# example = '8A004A801A8002F478'
# example = '620080001611562C8802118E34'
# example = 'C0015000016115A2E0802F182340'
# example = 'A0016C880162017C3686B18A3D4780'
# Part2
# example = 'C200B40A82'
# example = '04005AC33890'
# example = '880086C3E88112'
# example = 'CE00C43D881120'
# example = 'D8005AC2A8F0'
# example = 'F600BC2D8F'
# example = '9C005AC2F8F0'
# example = '9C0141080250320F1802104A08'
# outerPacket = Packet(hex=example)

inp = open("../../input/2021/16/input", 'r').read().splitlines()[0]
outerPacket = Packet(hex=inp)
print("Part 1:", outerPacket.version_sum())
print("Part 2:", outerPacket.value)
