#! /usr/bin python3

import math

class Rock:
    def __init__(self, shape, name):
        self.shape = shape
        self.height = len(shape)
        self.width = len(shape[0])
        self.name = name

class Jet:
    def __init__(self, pattern):
        self.pattern = []
        for d in pattern:
            d = 1 if d == '>' else 0
            self.pattern.append(d)
        self.pos = 0
        self.dir = self.pattern[0]

    def next(self):
        if self.pos < len(self.pattern) - 1:
            self.pos += 1
        else:
            self.pos = 0
        self.dir = self.pattern[self.pos]
        return self.dir

class Chamber:
    def __init__(self, width, height, jet):
        self.width = width
        self.state = [[0]*width for _ in range(height)]
        self.jet = jet
        self.shortened = 0
        # for signature
        self.cache = {}
        self.sig1 = None
        self.sig2 = None

    def print(self):
        print("size:", len(self.state), "x", self.width, ", Jet at", self.jet.pos, self.jet.dir)
        print("highest rock at", self.highest_rock())
        i = len(self.state) - 1 + self.shortened
        for l in self.state[::-1]:
            print(i, ''.join(['#' if e else '.' for e in l]))
            i -= 1

    def highest_rock(self):
        for i, l in enumerate(self.state):
            if not sum(l):
                return i - 1
        return -1

    def collision(self, rock, h, p):
        for i, l in enumerate(rock.shape):
            for j, y in enumerate(l):
                if self.state[i+h][j+p] and y:
                    return True
        return False

    def signature(self, rock):
        return (rock.name, self.jet.pos, tuple(map(tuple, self.state[-30:])))

    def falling(self, rock, rock_count):
        # rock appears (left edge 2 units away from chambers left wall, bottom edge 3 units above heighest rock)
        h = self.highest_rock() + 4 # /y pos
        p = 2 # x pos
        # extend chamber if necessary
        for _ in range(h - len(self.state) + rock.height):
            self.state.append([0 for _ in range(len(self.state[0]))])

        # OPTIMIZATION: while rock above rocks in chamber, concatenate movements
        # because no collision possible (or: only collision with wall possible)
        move = 0
        maxmove = self.width - 2 - rock.width
        minmove = -2
        for _ in range(3):
            if self.jet.dir:
                move = min(maxmove, move + 1)
            else:
                move = max(minmove, move - 1)
            self.jet.next()
        p += move
        h -= 3

        # while falling possible
        while True:
            # rock is getting pushed
            if self.jet.dir: # rigth
                if p + rock.width < self.width and not self.collision(rock, h, p+1): # enough space, no collision
                    p += 1
            else: # left
                if p > 0 and not self.collision(rock, h, p-1): #enough space, no collision
                    p -= 1
            self.jet.next()
            # rock falls
            if not self.collision(rock, h-1, p) and h > 0: # rock can fall
                h -= 1
            else: #rock is stuck
                for i, l in enumerate(rock.shape):
                    for j, y in enumerate(l):
                        self.state[i+h][j+p] += y
                        if self.state[i+h][j+p] > 1:
                            print("Error: state not allowed to exceed 1", i+h, j+p)
                            self.print()
                            exit()
                ## OPTIMIZATION: if TETRIS with two adjacent lines combined, cut bottom of chamber
                ## if full row (now previous) highest rock is filled
                #if min([sum(z) for z in zip(self.state[h], self.state[h-1])]) and h+self.shortened < 4000: # don't cut to small chunks
                #    self.shortened += h - 1
                #    self.state = self.state[h-1:]

                # cache signature
                sig = self.signature(rock)
                if h > 4000 and not self.sig1 and not self.sig2:
                    if sig not in self.cache:
                        self.cache[sig] = (h, rock_count)
                    else:
                        self.sig1 = self.cache[sig]
                        self.sig2 = (h, rock_count)
                break

inp = open("../../input/2022/17/input",  'r').read().splitlines()[0]

rocks = [Rock([[1, 1, 1, 1]], 'hline'), # -
        Rock([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 'plus'), # +
        Rock([[1, 1, 1], [0, 0, 1], [0, 0, 1]], 'capital L'), # L^-1
        Rock([[1], [1], [1], [1]], 'vline'), # |
        Rock([[1, 1], [1, 1]], 'square')] # o

chamber = Chamber(7, 4, Jet(inp))

rock_count = 0
cur_rock = 0
while rock_count < 2022:
    chamber.falling(rocks[cur_rock], rock_count)
    if cur_rock < len(rocks) - 1:
        cur_rock += 1
    else:
        cur_rock = 0
    rock_count += 1

print("Part 1:", chamber.highest_rock() + 1 + chamber.shortened)
factor = 0
while rock_count < 1_000_000_000_000: # trillion
    chamber.falling(rocks[cur_rock], rock_count)
    # check if signature was found
    if chamber.sig1 and chamber.sig2 and not factor:
        hd = chamber.sig2[0] - chamber.sig1[0]
        rd = chamber.sig2[1] - chamber.sig1[1]
        factor = math.floor((1_000_000_000_000 - rock_count) / rd)
        rock_count += rd * factor
    if cur_rock < len(rocks) - 1:
        cur_rock += 1
    else:
        cur_rock = 0
    rock_count += 1

print("Part 2:", chamber.highest_rock() + hd * factor + 1)

