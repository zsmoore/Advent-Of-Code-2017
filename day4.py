import sys

def main():
    in_file = open(sys.argv[1], 'r')

    total = 0
    for line in in_file.readlines():
        if is_valid(line.strip()):
            total += 1

    print(total)


def is_valid(passphrase):
    if len(set(passphrase.split())) < len(passphrase.split()):
        return False

    return True

if __name__ == "__main__":
    main()
