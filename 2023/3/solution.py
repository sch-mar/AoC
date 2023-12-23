import re

class Number:
    def __init__(self, index, pos, value):
        self.index = index
        self.pos = pos
        self.value = value
        self.len = len(str(value))
        self.is_partn = Number.has_adjacent_symbol(self)

    def has_adjacent_symbol(self):
        adj = ''
        top = bool(self.index > 0)
        left = bool(self.pos > 0)
        right = bool(self.pos + self.len < len(inp[0]))
        bottom = bool(self.index + 1 < len(inp))

        if left and top:
            adj += inp[self.index-1][self.pos-1]
        if top:
            adj += inp[self.index-1][self.pos:self.pos+self.len]
        if top and right:
            adj += inp[self.index-1][self.pos+self.len]

        if left:
            adj += inp[self.index][self.pos-1]
        if right:
            adj += inp[self.index][self.pos+self.len]

        if left and bottom:
            adj += inp[self.index+1][self.pos-1]
        if bottom:
            adj += inp[self.index+1][self.pos:self.pos+self.len]
        if bottom and right:
            adj += inp[self.index+1][self.pos+self.len]

        return bool(re.search(r'[^\d.]', adj))

    def __str__(self):
        if self.is_partn:
            return f'{self.value} at ({self.index}, {self.pos}), partnumber'
        else:
            return f'{self.value} at ({self.index}, {self.pos}), not partnumber'

class Asterisk:
    def __init__(self, index, pos):
        self.index = index
        self.pos = pos
        self.is_gear = Asterisk._has_exactly_2_adjacent_numbers(self)
        if self.is_gear:
            self.gear_ratio = Asterisk._calculate_gear_ratio(self)

    def _has_exactly_2_adjacent_numbers(self):
        number_counter = 0
        self.number_indices = []
        for i in range (max(0, self.index - 1), min(len(inp), self.index + 2)):
            number_counter += len(re.findall(r'\d+', inp[i][max(0,self.pos-1) : min(len(inp[0]),self.pos+2)]))
            for n in re.findall(r'\d+', inp[i][max(0,self.pos-1) : min(len(inp[0]),self.pos+2)]):
                self.number_indices.append(i)
        return bool(number_counter == 2)

    def _calculate_gear_ratio(self):
        ratio_parts = []
        if self.number_indices[0] == self.number_indices[1]:
            # first number
            for number in numbers:
                if number.index == self.number_indices[0] and self.pos - 1 in range(number.pos, number.pos+number.len):
                    ratio_parts.append(number.value)
            # second number
            for number in numbers:
                if number.index == self.number_indices[0] and self.pos + 1 in range(number.pos, number.pos+number.len):
                    ratio_parts.append(number.value)
        else:
            for ni in self.number_indices:
                ratio_parts.append(Asterisk._find_number(self, ni).value)
        return ratio_parts[0] * ratio_parts[1]

    def _find_number(self, index):
        for number in numbers:
            if number.index == index and set(range(max(0, self.pos-1), min(len(inp[0]), self.pos+2))) & set(range(number.pos, number.pos+number.len)):
                return number

#inp = open('../../input/2023/3/example1', 'r').read()[:-1].splitlines()
#inp = open('../../input/2023/3/example1test', 'r').read()[:-1].splitlines()
#inp = open('../../input/2023/3/anotherexample', 'r').read()[:-1].splitlines()
#inp = open('../../input/2023/3/example2', 'r').read()[:-1].splitlines()
#inp = open('../../input/2023/3/testcases', 'r').read()[:-1].splitlines()
inp = open('../../input/2023/3/input', 'r').read()[:-1].splitlines()

numbers = []

for index, line in enumerate(inp):
    lastpos = 0
    for number in re.findall(r'\d+', line):
        numbers.append(Number(index, re.compile(number).search(line, lastpos).span()[0], int(number)))
        lastpos = re.compile(number).search(line, lastpos).span()[0] + len(number)

print(f'Part 1: {sum([number.value for number in numbers if number.is_partn])}')

###############

asterisks = []

for index, line in enumerate(inp):
    lastpos = 0
    for asterisk in re.findall(r'\*', line):
        asterisks.append(Asterisk(index, re.compile('\*').search(line, lastpos).span()[0]))
        lastpos = re.compile('\*').search(line, lastpos).span()[0] + 1

print(f'Part 2: {sum([asterisk.gear_ratio for asterisk in asterisks if asterisk.is_gear])}')

