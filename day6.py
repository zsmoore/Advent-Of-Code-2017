import sys
import copy
from itertools import cycle

def main():
    in_file = open(sys.argv[1], 'r')

    banks = list(map(int, in_file.readline().strip().split()))

    print(compute_cycles(banks))

def compute_cycles(alist):
    states = [copy.copy(alist)]
    cycle_count = 0

    while True:
        max_index = find_highest(alist)
        alist = redistribute(alist, max_index)
        
        cycle_count += 1
        for state in states:
            if state == alist:
                return cycle_count                

        states.append(copy.copy(alist))

def redistribute(alist, highest_index):
    to_distribute = alist[highest_index]
    alist[highest_index] = 0

    curr_index = highest_index + 1
    while to_distribute > 0:
        if curr_index >= len(alist):
            curr_index = 0

        alist[curr_index] += 1
        curr_index += 1
        to_distribute -= 1
    return alist

def find_highest(alist):
    max_num = alist[0]
    max_index = 0
    for x in range(len(alist)):
        if alist[x] > max_num:
            max_num = alist[x]
            max_index = x
    return max_index

    
if __name__ == "__main__":
    main()
