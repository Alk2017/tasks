def check(clumbs):
    i = 0
    res = []
    for clumb in clumbs:
        if len(res) == 0:
            res.append(clumb)
            continue
        if clumb[0] <= res[i][1] < clumb[1]:
            res[i] = (res[i][0], clumb[1])
            continue
        if clumb[0] > res[i][1]:
            res.append(clumb)
            i += 1
    for item in res:
        print(f'{item[0]} {item[1]}')


def run():
    count = int(input())
    ls_in = list()
    for _ in range(count):
        ls_in.append(tuple(int(i) for i in input().split()))

    ls_in.sort(key=lambda x: (x[0], x[1]))
    check(ls_in)


if __name__ == '__main__':
    run()