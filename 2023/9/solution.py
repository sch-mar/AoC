
def predict(lines):
    while set(lines[-1]) != set([0]):
        lines.append([lines[-1][i+1]-lines[-1][i] for i in range(len(lines[-1])-1)])

    for i in range(len(lines)-2,-1,-1):
        lines[i].append(lines[i][-1] + lines[i+1][-1])

    return lines[0][-1]


#inp = [line.split() for line in open('../../input/2023/9/example1', 'r').read().splitlines()[:-1]]
inp = [line.split() for line in open('../../input/2023/9/input', 'r').read().splitlines()[:-1]]

for i in range(len(inp)):
    inp[i] = [int(j) for j in inp[i]]

predictions = [predict([value_history]) for value_history in inp]

print(f'Part 1: {sum(predictions)}')

