import sys

def main():
    in_file = open(sys.argv[1], 'r')

    total = 0
    for line in in_file.readlines():
        if is_valid(line.strip()) and check_anagram(line.strip()):
            total += 1

    print(total)


def is_valid(passphrase):
    if len(set(passphrase.split())) < len(passphrase.split()):
        return False

    return True

def is_anagram(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    return False

def check_anagram(passphrase):
    passphrase = set(passphrase.split())
    for word in passphrase:
        for word2 in passphrase:
            if word != word2 and is_anagram(word, word2):
                return False
    return True

if __name__ == "__main__":
    main()
