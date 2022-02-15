from random import randrange
import time


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
        for j in range(i, count):
            if ar[j] > ar[min_i]:
                min_i = j
        if min_i != i:
            ar[i], ar[min_i] = ar[min_i], ar[i]


def merge_sort(ar):
    count = len(ar)
    res = [] * count
    left = merge_sort(ar[0:count / 2])
    right = merge_sort(ar[count / 2:count])

    l, r, k = 0
    l_c = len(left)
    r_c = len(right)


def check(ls):
    for t in zip(ls, ls[1:]):
        assert t[0] <= t[1], f'{t[0]} > {t[1]}'


if __name__ == '__main__':
    res_choose = 0.0
    res_bubble = 0.0
    res_insert = 0.0
    a = [int(n) for n in
         '9 18 1 65 51 16 6 43 6 36 7 11 64 5 1 76 15 11 11 15 57 95 3 49 92 78 83 51 10 3'.split()]
    choose_sort(a)
    print(a)
    '9 95 92 83 78 7 76 6 6 65 64 57 5 51 51 49 43 36 3 3 18 16 15 15 11 11 11 1 1 10'

    for _ in range(0, 0):
        ar1 = [randrange(100) for _ in range(5000)]
        ar2 = ar1.copy()
        ar3 = ar2.copy()

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
    print(res_choose)
    print(res_bubble)
    print(res_insert)
