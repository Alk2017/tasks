def isequal(fr1, fr2, slen, h, x, p):
    return (
            (h[fr1 + slen] + h[fr2] * x[slen]) % p ==
            (h[fr2 + slen] + h[fr1] * x[slen]) % p
    )


def run():
    line = input()
    # line = 'acabaca'
    n = len(line)
    p = 10 ** 9 + 7
    x_ = 257
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    line = ' ' + line
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(line[i])) % p
        x[i] = (x[i - 1] * x_) % p
    for _ in range(int(input())):
        l, a, b = [int(i) for i in input().split()]
        if isequal(a, b, l, h, x, p):
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    run()
