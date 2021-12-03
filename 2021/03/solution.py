#!/usr/bin/env python3

from textwrap import wrap

report = [wrap(str(l).strip("\n"), 1) for l in open("input").readlines()]
reportsize = len(report) # number of lines in report

bitcounter = [int(0) for i in range(len(report[0]))]

for number in report:
    for i in range(len(number)):
        bitcounter[i] += int(number[i])

gammarate = []
epsilonrate = []

for c in bitcounter:
    if c>reportsize-c:
        gammarate.append('1')
        epsilonrate.append('0')
    else:
        gammarate.append('0')
        epsilonrate.append('1')

gammarate_binary = ''.join(gammarate)
gammarate_decimal = int(gammarate_binary, 2)
epsilonrate_binary = ''.join(epsilonrate)
epsilonrate_decimal = int(epsilonrate_binary, 2)

print(f"gammarate = {gammarate_binary} = {gammarate_decimal}")
print(f"epsilonrate = {epsilonrate_binary} = {epsilonrate_decimal}")
print(f"powerconsumption = {gammarate_decimal*epsilonrate_decimal}")

### part 2

# oxygen

oxygenreport = report.copy()
bitpos = 0
maxbitpos = len(oxygenreport[0])# - 1
counter = 0
commonbit = ''

while len(oxygenreport)>1:
    counter = 0
    for line in oxygenreport:
        if line[bitpos] == '1':
            counter += 1
    #print(counter)

    if counter>=len(oxygenreport)-counter:
        commonbit = '1'
    else:
        commonbit = '0'

    #print(commonbit)

    i = 0
    while i < len(oxygenreport):
        #print(i)
        #print(oxygenreport[i])
        if oxygenreport[i][bitpos] != commonbit:
            #print(f"popping {oxygenreport[i]}")
            oxygenreport.pop(i)
        else:
            i += 1

    #print(oxygenreport)

    if bitpos < maxbitpos:
        bitpos += 1
    else:
        bitpos = 0

oxygen_generator_rating_binary = ''.join(oxygenreport[0])
oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)

# co2

co2report = report.copy()
bitpos = 0
maxbitpos = len(co2report[0])
counter = 0
commonbit = ''

while len(co2report) > 1:
    counter = 0
    for line in co2report:
        counter += int(line[bitpos])

    if counter >=len(co2report)-counter:
        commonbit = '1'
    else:
        commonbit = '0'

    i = 0
    while i < len(co2report):
        if co2report[i][bitpos] == commonbit:
            #print(f"popping {co2report[i]}")
            co2report.pop(i)
        else:
            i += 1
    
    if bitpos < maxbitpos:
        bitpos += 1
    else:
        bitpos = 0

co2_scrubber_rating_binary = ''.join(co2report[0])
co2_scrubber_rating_decimal = int(co2_scrubber_rating_binary, 2)

print(f"\noxygen generator rating = {oxygen_generator_rating_binary} = {oxygen_generator_rating_decimal}")
print(f"co2 scrubber rating = {co2_scrubber_rating_binary} = {co2_scrubber_rating_decimal}")
print(f"life support rating = {oxygen_generator_rating_decimal*co2_scrubber_rating_decimal}")

