import sys
import pprint
import math
from itertools import cycle

def main():
    input_num = int(sys.argv[1])
    #grid = compute_spiral_grid_to_num(input_num)
    #print(find_distance(grid, input_num))
    grid = compute_growing_grid_to_num(input_num)
    print(find_end_value(grid, input_num))


def find_distance(grid, target):
    for tup in list(grid):
        if tup[0] == target:
            return tup[1][0] + tup[1][1]

def find_end_value(grid, num):
    res = sys.maxsize
    for alist in grid:
        for val in alist:
            if val and val > num and val < res:
                res = val
    return res

def move_right(x, y):
    return x + 1, y

def move_down(x, y):
   return x, y - 1

def move_left(x, y):
   return x - 1, y

def move_up(x, y):
   return x, y + 1

moves = [move_right, move_down, move_left, move_up]
_moves = cycle(moves)


def compute_spiral_grid_to_num(num):

    n = 1
    pos = 0, 0
    times_to_move = 1

    yield n, pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= num:
                    return 
                pos = move(*pos)
                n += 1
                yield n, pos

        times_to_move += 1

def compute_growing_grid_to_num(num):

    n = 1
    pos = ((int(math.sqrt(num)) + 1) // 2), ((int(math.sqrt(num)) + 1) // 2)
    times_to_move = 1

    grid = [[None for i in range(int(math.sqrt(num)) + 1)] for j in range(int(math.sqrt(num)) + 1)]
    grid[pos[0]][pos[1]] = n

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= num:
                    return grid 
                pos = move(*pos)
                n = compute_num(grid, pos)
                grid[pos[0]][pos[1]] = n

        times_to_move += 1

def compute_num(grid, pos):
    result = 0
    if grid[pos[0] - 1][pos[1]]:
        result += grid[pos[0] - 1][pos[1]]
    if grid[pos[0] + 1][pos[1]]:
        result += grid[pos[0] + 1][pos[1]]
    if grid[pos[0]][pos[1] - 1]:
        result += grid[pos[0]][pos[1] - 1]
    if grid[pos[0]][pos[1] + 1]:
        result += grid[pos[0]][pos[1] + 1]
    if grid[pos[0] + 1][pos[1] + 1]:
        result += grid[pos[0] + 1][pos[1] + 1]
    if grid[pos[0] - 1][pos[1] - 1]:
        result += grid[pos[0] - 1][pos[1] - 1]
    if grid[pos[0] - 1][pos[1] + 1]:
        result += grid[pos[0] - 1][pos[1] + 1]
    if grid[pos[0] + 1][pos[1] - 1]:
        result += grid[pos[0] + 1][pos[1] - 1]

    return result

if __name__ == "__main__":
    main()
