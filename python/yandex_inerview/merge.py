def merge(arr, lf, mid, rg):
    # Your code
    # “ヽ(´▽｀)ノ”
    i = 0
    res = [0] * rg
    l_i = lf
    r_i = mid
    while l_i < mid and r_i < rg and i < rg:
        if arr[l_i] <= arr[r_i]:
            res[i] = arr[l_i]
            l_i += 1
        else:
            res[i] = arr[r_i]
            r_i += 1
        i += 1
    while l_i < mid and i < rg:
        res[i] = arr[l_i]
        l_i += 1
        i += 1
    while r_i < rg and i < rg:
        res[i] = arr[r_i]
        r_i += 1
        i += 1
    return res


def merge_sort(arr, lf, rg):
    # TIME LIMITED=(
    if (rg - lf) > 1:
        mid = lf + (rg - lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)

        res = merge(arr, lf, mid, rg)
        j = 0
        for i in range(lf, rg):
            arr[i] = res[j]
            j += 1


def merge_2(arr, beg, mid, end, maxele):
    i = beg
    j = mid + 1
    k = beg

    while i <= mid and j <= end:
        if arr[i] % maxele <= arr[j] % maxele:
            arr[k] = arr[k] + (arr[i] %
                               maxele) * maxele
            k += 1
            i += 1
        else:
            arr[k] = arr[k] + (arr[j] %
                               maxele) * maxele
            k += 1
            j += 1

    while i <= mid:
        arr[k] = arr[k] + (arr[i] %
                           maxele) * maxele
        k += 1
        i += 1
    while j <= end:
        arr[k] = arr[k] + (arr[j] %
                           maxele) * maxele
        k += 1
        j += 1

    # Obtaining actual values
    for i in range(beg, end + 1):
        arr[i] = arr[i] // maxele


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
    # size = 100000
    # ar = [1] * size
    # merge_sort(ar, 0, size)
