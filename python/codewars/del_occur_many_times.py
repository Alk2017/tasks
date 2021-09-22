def delete_nth(order, max_e):
    m = {}
    res = []
    for i, s in enumerate(order):
        if s in m.keys():
            if m[s] >= max_e:
                continue
            m[s] += 1
        else:
            m[s] = 1
        res.append(s)
    return res


if __name__ == '__main__':
    print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
