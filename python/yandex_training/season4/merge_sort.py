def merge(ls1, ls2):
    i = j = 0
    f_1 = len(ls1) - 1
    f_2 = len(ls2) - 1
    res = []
    while i <= f_1 and j <= f_2:
        if ls1[i] <= ls2[j]:
            res.append(ls1[i])
            i += 1
        else:
            res.append(ls2[j])
            j += 1
    while i <= f_1:
        res.append(ls1[i])
        i += 1
    while j <= f_2:
        res.append(ls2[j])
        j += 1
    return res


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls) // 2
    h1 = merge_sort(ls[:mid])
    h2 = merge_sort(ls[len(h1):])
    return merge(h1, h2)


def run():
    input()
    ls = [int(i) for i in input().split()]
    # merge(ls1, 0, len(ls1) - 1, ls2, 0, len(ls2) - 1, res)
    print(' '.join([str(i) for i in merge_sort(ls)]))
    # print(merge_sort([9,3,6,1, 1, 1]))


if __name__ == '__main__':
    run()
