def swap(ls, i1, i2):
    ls[i1], ls[i2] = ls[i2], ls[i1]


def max_ch(ls, i, last_i):
    # last_i = len(ls) - 1
    lf_ch_i = 2 * i + 1
    rt_ch_i = 2 * i + 2
    if last_i < lf_ch_i:
        return -1
    elif last_i == lf_ch_i:
        return lf_ch_i
    elif ls[lf_ch_i] > ls[rt_ch_i]:
        return lf_ch_i
    else:
        return rt_ch_i


def sifting_down(ls, i, last_i):
    # last_i = len(ls) - 1
    max_ch_i = max_ch(ls, i, last_i)
    while ls[i] < ls[max_ch_i] and max_ch_i != -1:
        swap(ls, i, max_ch_i)
        i = max_ch_i
        max_ch_i = max_ch(ls, i, last_i)


def pyramid_sort(ls):
    last_i = len(ls) - 1
    last_unsort = (last_i - 1) // 2
    while last_unsort >= 0:
        sifting_down(ls, last_unsort, last_i)
        last_unsort -= 1
    # print(ls)
    while last_i > 0:
        swap(ls, 0, last_i)
        last_i -= 1
        sifting_down(ls, 0, last_i)
        # print(ls)


def run():
    count = int(input())
    ls = [int(i) for i in input().split()]
    pyramid_sort(ls)
    print(' '.join([str(i) for i in ls]))


if __name__ == '__main__':
    run()
