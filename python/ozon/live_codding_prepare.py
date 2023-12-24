def binary_search(ls, el, s, f):
    if s >= f:
        return -1
    m = (f + s) // 2
    if ls[m] > el:
        return binary_search(ls, el, s, m)
    elif ls[m] < el:
        return binary_search(ls, el, m + 1, f)
    elif ls[m] == el:
        return m


def binarySearch2(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binarySearch2(arr, x, left, mid)
    else:
        return binarySearch2(arr, x, mid + 1, right)


def run_2(m, el):
    a = [[2, 5, 7, 9],
         [11, 15, 17, 18],
         [24, 26, 29, 30]]
    b = 15
    h = len(a)
    if h == 0:
        return False
    w = len(a[0])
    if w == 0:
        return False
    h_el = -1
    for i in range(h):
        if el < a[i][0]:
            return False
        elif el <= a[i][-1]:
            h_el = i
            break
        else:
            if i == h - 1:
                return False


def run_1(ls_a, ls_b):
    i = j = 0
    s_a = len(ls_a)  # 1 1 3 4 .5 7   1 0 6 3
    s_b = len(ls_b)  # 1 3 4 .
    while i < s_a and j < s_b:
        if ls_a[i] <= ls_b[j]:
            i += 1
        else:
            ls_a.insert(i, ls_b[j])
            j += 1
            i += 1

            s_a += 1
    while j < s_b:
        ls_a.append(ls_b[j])
        j += 1


if __name__ == '__main__':
    # test_cases = [
    #     ([], []),
    #     ([1], [1]),
    #     ([1, 1], [1, 1]),
    #     ([1, 9], [1, 9]),
    #     ([0, 7, 9], [1, 5, 8]),
    # ]
    # for case in test_cases:
    #     run_1(case[0], case[1])
    #     print(case[0])
    # print(binary_search([1, 2, 2, 2, 3], 3, 0, 4))
    # print(binarySearch2([1, 2, 2, 2, 3], 3, 0, 4))
    pass
