import sys
def main():
    captcha = open(sys.argv[1], 'r').readline()

    result = compute_captcha(captcha)
    print(result)

def compute_captcha(captcha):
    result = 0

    matches = get_matches(captcha)
    for num in matches:
        result += int(num)

    return result

def get_matches(input_string):
    matches = []

    buff = input_string[-1]
    for char in input_string:
        if buff == char:
            matches.append(char)
        buff = char

    return matches

if __name__ == "__main__":
    main()
