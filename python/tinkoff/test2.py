def m1(num, res):
    if num == 1:
        return res
    else:
        res += 1
        return m1(my_round(num), res)


def my_round(i):
    if i / 2 % 1 >= 0.5:
        return i // 2 + 1
    else:
        return i // 2


if __name__ == '__main__':
    a = int(input())
    print(m1(a, 0))
