def run():
    n, k = [int(i) for i in input().split()]
    if k == 1 or n == 1:
        print(1)
        return
    res = [0] * n
    res[0] = 1
    res[1] = 1
    for j in range(2, n):
        first = 0 if k > j else j - k
        res[j] = sum(res[first:j])
    print(res[-1])


if __name__ == '__main__':
    run()
