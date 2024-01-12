from sympy import solve_univariate_inequality, Symbol, sin, Interval, S
import math

def d(t_r, t_c): # get distance travelled, using racte time and charging time 
    return (t_r*t_c) - pow(t_c, 2)

def margin(t, d):
    x = Symbol('x')
    start = solve_univariate_inequality(t*x-x**2>d, x, relational=False).start
    end = solve_univariate_inequality(t*x-x**2>d, x, relational=False).end
    return math.ceil(end) - math.floor(start) - 1

#inp = open('../../input/2023/6/example1', 'r').read().splitlines()[:-1]
inp = open('../../input/2023/6/input', 'r').read().splitlines()[:-1]

time = [int(i) for i in inp[0].split()[1:]]
dist = [int(i) for i in inp[1].split()[1:]]
marg = []

for i in range(len(time)):
    marg.append(margin(time[i], dist[i]))

print(f'Part 1: {math.prod(marg)}')

##########

time = int(''.join([str(i) for i in time]))
dist = int(''.join([str(i) for i in dist]))

print(f'Part 2: {margin(time, dist)}')

