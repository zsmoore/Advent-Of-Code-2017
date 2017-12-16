import sys
import copy

def main():
    in_file = open(sys.argv[1], 'r')
    
    jumps = []
    for line in in_file.readlines():
        jumps.append(int(line.strip()))

    #print(compute_exit(jumps))
    print(compute_exit2(jumps))

def compute_exit(jump_list):
    current_ind = 0
    step_num = 0
    while True:
        if current_ind < 0 or current_ind >= len(jump_list):
            return step_num

        step = jump_list[current_ind]
        jump_list[current_ind] += 1
        current_ind += step
        step_num += 1
        
def compute_exit2(jump_list):
    current_ind = 0
    step_num = 0
    while True:
        if current_ind < 0 or current_ind >= len(jump_list):
            return step_num

        step = jump_list[current_ind]
        if step >= 3:
            jump_list[current_ind] -= 1
        elif step <= -3:
            jump_list[current_ind] += 1
        else:
            jump_list[current_ind] += 1

        current_ind += step
        step_num += 1

if __name__ == "__main__":
    main()
