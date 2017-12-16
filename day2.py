import sys

def main():
    in_file = open(sys.argv[1], 'r')
    diffs = []
    for line in in_file.readlines():
        #diffs.append(compute_checksum(line))
        diffs.append(compute_divisible(line))

    print(sum(diffs))     

def compute_checksum(a_line):
    line = a_line.split()
    line = list(map(int, line))
    minimum = min(line)
    maximum = max(line)

    return maximum - minimum

def compute_divisible(a_line):
    line = a_line.split()
    line = list(map(int, line))
    for x in range(len(line)):
        for y in range(len(line)):
            if x != y:
                if (line[x] / line[y]).is_integer():
                    return line[x] / line[y]
    return 0

if __name__ == "__main__":
    main()
