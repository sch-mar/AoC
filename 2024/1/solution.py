inp = open("../../input/2024/1/input", 'r').read().splitlines()[:-1]

left = []
right = []

for line in inp:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

distances = []

for i in range(len(left)):
    distances.append(abs(left[i]-right[i]))

print(f'The total distance between the lists is {sum(distances)}.')

#-------

similarities = []

right_counted = {r: 0 for r in set(right)}
for r in right:
    right_counted[r] += 1

for l in left:
    try:
        similarities.append(l*right_counted[l])
    except KeyError:
        continue

print(f'The similarity score is {sum(similarities)}.')

