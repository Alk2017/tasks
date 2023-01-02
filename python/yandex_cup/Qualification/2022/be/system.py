ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base

    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += ALPHABET[m]
    return res[::-1]


def run():
    line = input()
    min_s = 2
    for ch in line:
        if ch in ALPHABET and ALPHABET.index(ch) + 1 > min_s:
            min_s = ALPHABET.index(ch) + 1
    # equetion = line.split()
    avg = line.index('=')

    for b in range(min_s, 37):
        left = []
        right = []
        minus = False
        i = 0
        while i != len(line):
            num = ''
            if line[i] == '-':
                i += 1
                minus = True
                continue
            elif line[i] == '+' or line[i] == ' ' or line[i] == '=':
                i += 1
                continue
            else:
                while i != len(line) and line[i] in ALPHABET:
                    num += line[i]
                    i += 1
                if i < avg:
                    left.append(int(convert_base(num, from_base=b)) * (
                        -1 if minus else 1))
                else:
                    right.append(int(convert_base(num, from_base=b)) * (
                        -1 if minus else 1))
                minus = False
        if sum(left) == sum(right):
            print(b)
            break
    else:
        print('-1')


if __name__ == '__main__':
    run()
# 0-9 = 48-57, A-Z = 65-90, '=' = 61, '+' = 43, '-' = 45
