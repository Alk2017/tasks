def check(num):
    res = []
    for i in range(13, -1, -1):
        res.append(num // 2 ** i)
        num %= 2 ** i
    return res[res.index(1):]


if __name__ == '__main__':

    # num = int(input())
    # print(''.join(map(lambda i: str(i), check(num))))
