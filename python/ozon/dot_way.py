def neib(f, d):
    i, j = d
    c = []
    h = len(f) - 1
    w = len(f[0]) - 1
    if i == 0 and j == 0:
        if w > 0:
            c.append((i, j+1) if f[i][j + 1] == '*' else None)
        if h > 0:
            c.append((i+1, j) if f[i + 1][j] == '*' else None)
    elif i == 0 and j < w:
        c.append((i, j+1) if f[i][j + 1] == '*' else None)
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        if h > 0:
            c.append((i+1, j) if f[i + 1][j] == '*' else None)
    elif i == 0 and j == w:
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        if h > 0:
            c.append((i+1, j) if f[i + 1][j] == '*' else None)
    elif i < h and j == 0:
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
        c.append((i+1, j) if f[i + 1][j] == '*' else None)
        if w > 0:
            c.append((i, j+1) if f[i][j + 1] == '*' else None)
    elif i == h and j == 0:
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
        if w > 0:
            c.append((i, j+1) if f[i][j + 1] == '*' else None)
    elif i == h and j < w:
        c.append((i, j+1) if f[i][j + 1] == '*' else None)
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
    elif i == h and j == w:
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
    elif i < h and j == w:
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
        c.append((i+1, j) if f[i + 1][j] == '*' else None)
    else:
        c.append((i, j-1) if f[i][j - 1] == '*' else None)
        c.append((i, j+1) if f[i][j + 1] == '*' else None)
        c.append((i-1, j) if f[i - 1][j] == '*' else None)
        c.append((i+1, j) if f[i + 1][j] == '*' else None)
    return list(filter(lambda a: a is not None, c))


def direct(d1, d2):
    if (d2[0] - d1[0]) == 1:
        return 'D'
    elif (d2[0] - d1[0]) == -1:
        return 'U'
    elif (d2[1] - d1[1]) == 1:
        return 'R'
    elif (d2[1] - d1[1]) == -1:
        return 'L'


def run():
    c = int(input())
    for _ in range(c):
        f = []
        res = ''
        n = None
        dot = None
        h, w = [int(i) for i in input().split()]
        for _ in range(h):
            f.append(list(input()))
        for i in range(h):
            if dot is None:
                for j in range(w):
                    if f[i][j] == '*':
                        nbs = neib(f, (i, j))
                        if len(nbs) == 1:
                            n = nbs[0]
                            dot = (i, j)
                            break
        while len(res) == 0 or len(neib(f, dot)) != 1:
            res += direct(dot, n)
            neibs = neib(f, n)
            neibs.remove(dot)
            dot = n
            if len(neibs) == 0:
                break
            n = neibs[0]
        print(res)


if __name__ == '__main__':
    run()

"""
.*....
.*.***
.***.*
.....*
......

"""
