import time
from random import randrange


def insert_sort(ar):
    for i in range(1, len(ar)):
        j = i
        el = ar[i]
        while j > 0 and el < ar[j - 1]:
            ar[j] = ar[j - 1]
            j -= 1
        ar[j] = el
        # print(ar)


def bubble_sort(ar):
    count = len(ar)
    swap_c = 1
    while swap_c != 0:
        swap_c = 0
        for i in range(1, count):
            if ar[i] < ar[i - 1]:
                ar[i], ar[i - 1] = ar[i - 1], ar[i]
                swap_c += 1


def bubble_sort_v2(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_v3(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


def choose_sort(ar):
    count = len(ar)
    for i in range(count):
        min_i = i
        for j in range(i+1, count):
            if ar[j] < ar[min_i]:
                min_i = j
        if min_i != i:
            ar[i], ar[min_i] = ar[min_i], ar[i]


def merge_sort(ar):
    count = len(ar)
    if count == 1:
        return ar
    res = [0] * count
    left = merge_sort(ar[0: count // 2])
    right = merge_sort(ar[count // 2: count])

    l = r = k = 0
    l_c = len(left)
    r_c = len(right)

    while l < l_c and r < r_c:
        if left[l] <= right[r]:
            res[k] = left[l]
            l += 1
        else:
            res[k] = right[r]
            r += 1
        k += 1
    while l < l_c:
        res[k] = left[l]
        k += 1
        l += 1
    while r < r_c:
        res[k] = right[r]
        k += 1
        r += 1
    return res


def quick_sort(ar):
    size = len(ar)
    if size == 0 or size == 1:
        return ar
    left = []
    right = []
    middle = []
    support = ar[size//2]
    for el in ar:
        if el > support:
            right.append(el)
        elif el < support:
            left.append(el)
        else:
            middle.append(el)
    return quick_sort(left) + middle + quick_sort(right)


def check(ls):
    for t in zip(ls, ls[1:]):
        assert t[0] <= t[1], f'{t[0]} > {t[1]}'


# Pyramid sort =================
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

# =========================================


if __name__ == '__main__':
    res_choose = 0.0
    res_bubble = 0.0
    res_insert = 0.0
    res_merge = 0.0
    res_quick = 0.0
    res_pyramid = 0.0

    for _ in range(0, 1):
        ar1 = [randrange(100) for _ in range(10000)]
        ar2 = ar1.copy()
        ar3 = ar2.copy()
        ar4 = ar3.copy()
        ar5 = ar4.copy()
        ar6 = ar5.copy()

        # print(ar1)
        time1 = time.time()
        choose_sort(ar1)
        res_choose += time.time() - time1
        # print(f'choose sort - {time2}')
        # print(ar1)
        check(ar1)

        # print(ar2)
        time1 = time.time()
        bubble_sort_v3(ar2)
        res_bubble += time.time() - time1
        # print(f'bubble sort - {time2}')
        # print(ar2)
        check(ar2)

        # ar3 = [11, 2, 9, 7, 1]
        # print(ar3)
        time1 = time.time()
        insert_sort(ar3)
        res_insert += time.time() - time1
        # print(f'insert sort - {time2}')
        # print(ar3)
        check(ar3)

        # print(ar4)
        time1 = time.time()
        ar4 = merge_sort(ar4)
        res_merge += time.time() - time1
        # print(f'insert sort - {time2}')
        # print(ar4)
        check(ar4)

        # print(ar5)
        time1 = time.time()
        ar5 = quick_sort(ar5)
        res_quick += time.time() - time1
        # print(f'quick sort - {time2}')
        # print(ar5)
        check(ar5)

        # print(ar6)
        time1 = time.time()
        pyramid_sort(ar6)
        res_pyramid += time.time() - time1
        # print(ar6)
        check(ar6)




    print(res_choose)
    print(res_bubble)
    print(res_insert)
    print(res_merge)
    print(res_quick)
    print(res_pyramid)
