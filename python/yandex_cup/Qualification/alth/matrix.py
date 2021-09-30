def build_matrix(d, w):
    res = []
    value = 1
    for _ in range(0, d):
        line_ar = []
        for _ in range(0, w):
            line_ar.append(value)
            value += 1
        res.append(line_ar)
    return res


def print_matrix(matrix):
    for i, n in enumerate(matrix):
        for m in n:
            print(m, end=' ')
        print('')


def fold_matrix(matrix):
    res = []
    d = len(matrix)
    w = len(matrix[0])
    new_w = w // 2
    s = set()
    if d < w:
        for z in range(0, d):
            value = [matrix[z][0] + matrix[z][-1]]
            s.add(value[0])
            res.append(new_w * value)
    else:
        line_ar = [a + b for a, b in zip(matrix[0], matrix[-1])]
        s.update(line_ar)
        for _ in range(0, d // 2):
            res.append(line_ar)
    return res, s


if __name__ == '__main__':
    i, j = map(lambda _: int(_), input().split())
    # i, j = 8, 18
    m = build_matrix(i, j)
    s = set(range(1, (j * i + 1)))
    # print_matrix(m)
    while len(m) != 1 or len(m[0]) != 1:
        m, new_s = fold_matrix(m)
        s = s.union(new_s)
        # print_matrix(m)
    print(len(s))
