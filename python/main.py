if __name__ == '__main__':
    a = [1, 4]
    b = [3, 3]
    c = [2, 6]
    d = [1, 3]
    z = {}
    z[0] = a
    z[1] = b
    z[2] = c
    z[3] = d
    a = [0, 1, 2, 3]
    g = 'zopa'
    print(f'{g[0]}{len(g)-2}{g[-1]}')
    print(a[-2:])
    a.sort(key=lambda x:z[x])
    # s.sort(key=operator.itemgetter(1, 2))
    print(a)
    print(len(str(113)))
