import re

inp = open("../../input/2023/1/input", 'r').read().splitlines()

cv = [] # calibration values

for line in inp:
    digits = re.sub('[^\d]', '', line)
    cv.append(int(digits[0]+digits[-1]))

print(f'Part 1: {sum(cv)}')

##################

cv = []
dd = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
ddr = {key[::-1]: value for key, value in dd.items()}

for line in inp:
    d1 = re.search('(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\d', line)[0]
    if len(d1) > 1:
        d1 = dd[d1]
    d2 = re.search('(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)|\d', line[::-1])[0]
    if len(d2) > 1:
        d2 = ddr[d2]

    cv.append(int(d1+d2))

print(f'Part 2: {sum(cv)}')

