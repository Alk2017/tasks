import time


def get_m(ls, m, s=0, f=None):
    size = len(ls)
    if f is None:
        f = size - 1
    mid = s + (f - s) // 2
    if ls[mid] < m:
        if mid == size - 1:
            return size
        elif ls[mid + 1] >= m:
            return mid + 1
        else:
            return get_m(ls, m, mid + 1, f)
    elif ls[mid] >= m:
        if mid == 0:
            return 0
        else:
            if ls[mid - 1] < m:
                return mid
            return get_m(ls, m, s, mid)


def run():
    file_in = open('input.txt', 'r')
    # input()
    file_in.readline()
    t1 = time.time()
    # my_c_set = set([int(i) for i in input().split()])
    my_c_set = set([int(i) for i in file_in.readline().split()])
    my_c = list(my_c_set)
    my_c.sort()
    t2 = time.time()
    # input()
    file_in.readline()
    # other_c = [int(i) for i in input().split()]
    other_c = [int(i) for i in file_in.readline().split()]
    file_in.close()
    file_out = open("output.txt", "a")
    tm = time.time()
    for min_c in other_c:
        if min_c == 0 or len(my_c) == 0:
            # print('0')
            file_out.write('0\n')
            continue
        # i = 0
        # while i < len(my_c) and my_c[i] < min_c:
        #     i += 1
        # print(get_m(my_c, min_c))
        file_out.write(f'{get_m(my_c, min_c)}\n')
    # print(f'TIME: {time.time() - tm}')
    # print(f'TIME1: {t2 - t1}')
    file_out.close()


if __name__ == '__main__':
    run()

# if __name__ == '__main__':
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     m = 0
#     for i in range(-5, len(a) + 5):
#         print(f'{i} - {get_m(a, i)}')

