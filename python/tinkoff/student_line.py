from random import randrange


def run(ls=None):
    # input()
    if ls is None:
        ls = [int(i) for i in input().split()]
    need_swap = 0
    even = odd = -1

    for i, h in enumerate(ls):
        if (i + 1) % 2 != h % 2:
            if need_swap > 1:
                return -1, -1
            elif even == -1 and h % 2 == 0:
                even = i + 1
                need_swap += 1
            elif odd == -1 and h % 2 == 1:
                odd = i + 1
                need_swap += 1
            else:
                return -1, -1
    if need_swap != 2:
        return -1, -1
    # ls[odd - 1], ls[even - 1] = ls[even - 1], ls[odd - 1]
    # print(ls)
    if odd > even:
        return even, odd
    else:
        return odd, even


def run2(ls=None):
    input()
    if ls is None:
        ls = [int(i) for i in input().split()]
    odds = []
    evens = []
    for i, h in enumerate(ls):
        if (i + 1) % 2 != h % 2:
            if h % 2 == 0:
                evens.append(i + 1)
            else:
                odds.append(i + 1)
    if len(odds) == 1 and len(evens) == 1:
        return odds[0], evens[0]
    else:
        return -1, -1


def check(ls):
    odds = []
    evens = []
    for i, h in enumerate(ls):
        if (i + 1) % 2 != h % 2:
            if h % 2 == 0:
                evens.append(i + 1)
            else:
                odds.append(i + 1)
    if len(odds) == 1 and len(evens) == 1:
        return True
    else:
        return False


def gen(n):
    for _ in range(n):
        ls = [randrange(1, 11) for _ in range(7)]
        print(f'{ls} - {run2(ls)} - {check(ls)}')
        if run2(ls) == (-1, -1) and check(ls):
            print('!!!')


if __name__ == '__main__':
    # res = run()
    res = run2()
    print(f'{res[1]} {res[0]}')
    # check([8, 4, 1, 2, 5, 9, 9])
    # gen(100)