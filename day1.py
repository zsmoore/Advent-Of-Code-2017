import sys
def main():
    captcha = open(sys.argv[1], 'r').readline().strip()

    #result = compute_captcha(captcha)
    result = compute_captcha2(captcha)
    print(result)

def get_halfway(captcha):
    halves = []
    
    half = len(captcha) / 2
    for x in range(len(captcha)):
        num = captcha[x]
        ind = int(x + half)
        if ind > len(captcha) - 1:
            ind = ind - len(captcha)
        if num == captcha[ind]:
            halves.append(num)

    return halves

def compute_captcha2(captcha):
    result = 0

    halves = get_halfway(captcha)
    for num in halves:
        result += int(num)

    return result

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
