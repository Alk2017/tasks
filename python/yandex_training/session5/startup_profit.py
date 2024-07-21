def run():
    n, k, d = [int(i) for i in input().split()]
    res = n
    for j in range(d):
        for i in range(10):
            new = int(f'{res}{i}')
            if new % k == 0:
                if i == 0:
                    a = '0'*(d - (len(str(res)) - len(str(n))))
                    res = int(f'{res}{a}')
                    print(res)
                    return
                res = new
                # print(res)
                break
        else:
            res = -1
        if res == -1:
            print(res)
            break
    else:
        print(res)


if __name__ == '__main__':
    run()