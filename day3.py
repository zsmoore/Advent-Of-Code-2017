import sys
import pprint
from itertools import cycle

def main():
    input_num = int(sys.argv[1])
    grid = compute_grid_to_num(input_num)
    print(find_distance(grid, input_num))

def find_distance(grid, target):
    for tup in list(grid):
        if tup[0] == target:
            return tup[1][0] + tup[1][1]

def compute_grid_to_num(num):

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

if __name__ == "__main__":
    main()
