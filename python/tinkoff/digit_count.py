def get_digit(n):
    digit = 1
    while n // 10 != 0:
        n //= 10
        digit += 1
    return digit


def run(t=map(lambda i: int(i), input().split())):
    # =map(lambda i: int(i), input().split())
    l, r = t
    res = 0
    if l > r:
        print(res)
        return
    dig_l = get_digit(l)
    dig_r = get_digit(r)
    div_l = int('1' * dig_l)

    if dig_r == dig_l:
        if dig_r == 1:
            print(r - l + 1)
            return
        res += r // div_l - ((l - 1) // div_l)
    else:
        res += ((dig_r - dig_l) - 1) * 9
        div_r = int('1' * dig_r)
        res += r // div_r
        res += 9 - ((l - 1) // div_l)
    # if l/div_l > l//div_l:
    #     res -= 1
    print(res)
    return


def check(t):
    res = 0
    for i in range(t[0], t[1] + 1):
        j = len(str(i))
        if i % int('1' * j) == 0:
            res += 1
    assert run(t) == res, f'{t}: {run(t)} != {res}'


if __name__ == '__main__':
    run()
    # print(3<3.5)
    # check((1, 1000))
    # for i in range(1, 1111):
    #     for j in range(i, 1111):
    #         check((i, j))
