def partition(ls, ref_el, f_i, l_i):
    if l_i < f_i:
        return ls
    while f_i != l_i:
        if ls[f_i] < ref_el:
            f_i += 1
            continue
        elif ls[l_i] >= ref_el:
            l_i -= 1
            continue
        ls[f_i], ls[l_i] = ls[l_i], ls[f_i]
    return ls


def partition2(ls, e, f_i, l_i):
    if l_i < f_i:
        return -1, -1
    ref_el = ls[e]
    n = f_i
    g = -1
    while ls[n] < ref_el:
        n += 1
    if ls[n] == ref_el and n != e:
        ls[n], ls[n + 1] = ls[n + 1], ls[n]
        ls[e], ls[n] = ls[n], ls[e]
        e = n
        n += 2
    elif ls[n] == ref_el and n == e:
        n += 1
    elif ls[n] > ref_el:
        if e != n + 1:
            ls[n], ls[n + 1] = ls[n + 1], ls[n]
        ls[e], ls[n] = ls[n], ls[e]
        e = n
        g = n + 1
        n += 2
    for i in range(n, l_i + 1):
        if ref_el < ls[i]:
            # 1 2 5 5 8 9
            if g == -1:
                g = n
            n += 1
        elif ref_el > ls[i]:
            if g == -1:
                # 1 2 5 5 3 -> 1 2 3 5 5
                ls[e], ls[n] = ls[n], ls[e]
            else:
                # 1 2 5 5 7 3 -> 1 2 3 5 5 7
                ls[e], ls[g], ls[n] = ls[n], ls[e], ls[g]
                g += 1
            n += 1
            e += 1
        else:
            if g != -1:
                # 1 2 5 5 7 5 -> 1 2 5 5 5 7
                ls[g], ls[n] = ls[n], ls[g]
                g += 1
            n += 1
    return e, g


def partition3(ls, e, f_i, l_i):
    if l_i < f_i:
        return -1, -1
    ref_el = ls[e]
    n = g = e = f_i
    for i in range(f_i, l_i + 1):
        if ref_el < ls[i]:
            # 4 2 5 5 8 9
            # g = n
            pass
        elif ref_el > ls[i]:
            # 1 ->
            # 1 3 5 5 7 9 2 X -> 1 3 2 5 5 7 9 X
            ls[n], ls[g], ls[e] = ls[g], ls[e], ls[n]
            g += 1
            e += 1
        else:
            ls[g], ls[n] = ls[n], ls[g]
            g += 1
        n += 1
    return e, g


# 1 2 5 6 4


def quick_sort(ls, f_i, l_i):
    if l_i - f_i < 1 or l_i < 0 or f_i < 0:
        return
    ref_i = f_i + (l_i - f_i) // 2
    # ref_el = ls[ref_i]
    e, g = partition3(ls, ref_i, f_i, l_i)
    # ref_i = ls.index(ref_el)
    quick_sort(ls, f_i, e - 1)
    quick_sort(ls, g, l_i)


def run():
    input()
    ls = [int(i) for i in input().split()]
    # ls = [3, 5, 9, 1, 2, 5, 7]
    # el = int(input())
    # el = 2
    quick_sort(ls, 0, len(ls) - 1)
    # partition3(ls, 5, 0, len(ls) - 1)
    print(' '.join([str(i) for i in ls]))
    # file_out = open("output.txt", "a")
    # file_out.write(' '.join([str(i) for i in ls]))
    # file_out.close()


if __name__ == '__main__':
    run()
