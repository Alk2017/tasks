def run():
    _, c_r = [int(i) for i in input().split()]
    ls = [int(i) for i in input().split()]
    for _ in range(c_r):
        f, l = [int(i) for i in input().split()]
        min_n = min(ls[f:l+1])
        for i in range(f, l+1):
            if min_n < ls[i]:
                print(ls[i])
                break
        else:
            print('NOT FOUND')


if __name__ == '__main__':
    run()