def num_to_list(number):
    res = []
    while number != 0:
        res.append(number % 10)
        number //= 10
    res.reverse()
    return res


if __name__ == '__main__':
    res = set()
    for i in range(1, 100000000):
        n = 3 * i / sum(num_to_list(i)) ** 2
        if n % 1 == 0:
            res.add(int(n))
    ls = list(res)
    ls.sort()
    sh = 1
    # print(ls)
    for i in range(0, len(ls)):
        if ls[i] != i + sh:
            print(i + sh)
            break
