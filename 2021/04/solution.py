#! /usr/bin python3

def board_to_int_list(b): # get string from input and turn into int list
    o = []
    for line in b:
        o.append([int(line[i:i+2]) for i in range(0, len(line), 3)])
    return o

def remove_number_from_board(b, n):
    for i in range(5):
        for j in range(5):
            if b[i][j] == n:
                b[i][j] = None
                break
        else:
            continue
        break
    return b

def check_board_for_bingo(b): # check if board has full row or column of null
    for l in b:
        if l==[None for i  in range(5)]:
            return True
    b2 = [[row[i] for row in b] for i in range(5)]
    for l in b2:
        if l==[None for i  in range(5)]:
            return True
    return False

def sum_of_board(b):
    sum = 0
    for l in b:
        for c in l:
            if c!=None:
                sum += c
    return sum

## part 1

# get input

inp = [str(l).strip("\n") for l in open("input").readlines()]

# compute input

nums = list(map(int, inp[0].split(",")))

boards = []

for i in range(1, len(inp), 6):
    boards.append(board_to_int_list(inp[i+1:i+6]))

# play bingo

score = 0
bingo = False

for n in nums:
    for board in boards:
        board = remove_number_from_board(board, n)
        bingo = check_board_for_bingo(board)
        if bingo:
            score = sum_of_board(board) * n
            break
    else:
        continue
    break

print(f"score for first winning board: {score}")

## part 2

nums = list(map(int, inp[0].split(",")))

boards = []

for i in range(1, len(inp), 6):
    boards.append(board_to_int_list(inp[i+1:i+6]))

# play bingo

score = 0

bc = 0 # counter for boards

for n in nums:
    while len(boards)>0:
        boards[bc] = remove_number_from_board(boards[bc], n)
        if check_board_for_bingo(boards[bc]):
            score = sum_of_board(boards[bc]) * n
            boards.pop(bc)
            if bc==len(boards):
                bc=0
        else:
            if bc<len(boards)-1:
                bc += 1
            else:
                bc = 0
                break
    if len(boards)==0:
        break

print(f"score for last winning board: {score}")



