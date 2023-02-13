def sc_by_c(ss):
    res = dict()
    for s in ss:
        if s in res.keys():
            res[s] += 1
        else:
            res[s] = 1
    return res


def sc_by_p(sbc):
    res = dict()
    su = list(sbc.keys())
    su.sort()
    pl = 1
    d = 0
    for i, s in enumerate(su):
        if i != 0 and (s - su[i - 1]) > 1:
            pl += d
            d = sbc[s]
        else:
            d += sbc[s]
        res[s] = pl
    return res


def run():
    for _ in range(int(input())):
        c = int(input())
        s = [int(i) for i in input().split()]
        if c == 1:
            print('1')
            continue
        dbc = sc_by_c(s)
        dbp = sc_by_p(dbc)
        res = [str(dbp[i]) for i in s]
        print(' '.join(res))


if __name__ == '__main__':
    run()