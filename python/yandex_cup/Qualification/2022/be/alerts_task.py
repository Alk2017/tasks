import time
from random import random


def run(nxk=None, alerts=None):
    if nxk is None:
        n, x, k = [int(i) for i in input().split()]
    else:
        n, x, k = nxk
    if alerts is None:
        alts = [int(i) for i in input().split()]
    else:
        alts = list(alerts)
    alts.sort()
    res = []
    f = alts[0]
    for _ in range(k):
        res.append(f)
        f += x
    alts.remove(alts[0])
    while len(alts) > 0 and alts[0] < res[-1]:
        f = alts[0]
        if f in res:
            alts.remove(f)
            continue
        while f < res[-1]:
            res.remove(res[-1])
            res.append(f)
            res.sort()
            f += x
        alts.remove(alts[0])
    else:
        print(res[-1])
        return res[-1]


def run3(nxk=None, alerts=None):
    if nxk is None:
        n, x, k = [int(i) for i in input().split()]
    else:
        n, x, k = nxk
    if alerts is None:
        alts = [int(i) for i in input().split()]
    else:
        alts = list(alerts)
    times = []
    times.append(time.time())
    res = []
    alts.sort()
    times.append(time.time())
    while len(res) < k:
        i = 0
        if alts[i] in res:
            alts.remove(alts[i])
            continue
        res.append(alts[i])
        if (alts[i] + x) in alts:
            alts.remove(alts[i])
            continue
        alts[i] += x
        deep = k + 1 - len(res)
        # while len(alts) > i+1 and alts[i] > alts[i+1]:
        while len(alts) > i + 1 and alts[i] > alts[i + 1] and deep > 0:
            alts[i], alts[i + 1] = alts[i + 1], alts[i]
            i += 1
            deep -= 1

    else:
        times.append(time.time())
        print(res[-1])
        print(f'Time sort: {times[1] - times[0]}\n'
              f'time alth: {times[2] - times[1]}\n'
              f'time common:{times[2] - times[0]}\n')
        return res[-1]


def run4(nxk=None, alerts=None):
    if nxk is None:
        n, x, k = [int(i) for i in input().split()]
    else:
        n, x, k = nxk
    if alerts is None:
        alts = [int(i) for i in input().split()]
    else:
        alts = list(alerts)
    al_gr = {}
    times = []
    times.append(time.time())
    for a in alts:
        if a % x not in al_gr.keys():
            al_gr[a % x] = a
        else:
            al_gr[a % x] = min(al_gr.get(a % x), a)
    alts = list(al_gr.values())
    times.append(time.time())
    t_min = min(alts)
    t_max = t_min + x*k
    c_al = [0]*t_max
    for i in range(t_min, t_max):
        for al in alts:
            if i < al:
                pass
            elif i > al:
                c_al[i] += ((i - al) // x) + 1
            else:
                c_al[i] += 1
    times.append(time.time())
    print(c_al.index(k))
    times.append(time.time())
    print(f'Time sort equals: {times[1] - times[0]}\n'
          f'time alth: {times[2] - times[1]}\n'
          f'time search: {times[3] - times[2]}\n'
          f'time common:{times[3] - times[0]}\n')
    return c_al.index(k)


if __name__ == '__main__':
    count = 10
    flag = (False, [], [])
    # for _ in range(10000):
    for _ in range(1):
        # nxk = [count, 7, 10 ** 4]
        # a = [1, 2, ]
        nxk = [count, int(random() * 10**1)+1, int(random() * 10**1)+1]
        a = [int(random() * 10 ** 2) + 1 for _ in range(0, count)]
        b = run(nxk, a)
        c = run4(nxk, a)
        if b != c:
            print('fail')
            flag = (True, nxk, a)
    if flag[0]:
        print(f'nxt: {flag[1]} alerts:{flag[2]}')
    # run3()
    # https://contest.yandex.ru/contest/19036/problems/B
