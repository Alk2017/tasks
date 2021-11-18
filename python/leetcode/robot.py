def print_map(deep, weight, array):
    for i in range(deep):
        print('   ', end='')
        print(' -  ' * weight, end='')
        print()
        print(f'{deep - i - 1} ', end='')
        for j in range(weight):
            # if i == deep - 1 and j == 0:
            #     cell = 'R'
            # elif i == 0 and j == weight - 1:
            #     cell = 'X'
            # else:
            #     cell = ' '
            cell = array[i][j]
            print(f'| {cell} ', end='')
        print('|')
    print('   ', end='')
    print(' -  ' * weight, end='')
    print()
    print('   ', end='')
    for j in range(weight):
        print(f' {j}  ', end='')
    print()


def check(m, n, count=0):
    # print(f'm = {m}, n = {n} check')
    if m == 0 and n == 0:
        return count + 1
    elif m == 0:
        return check(m, n - 1, count)
    elif n == 0:
        return check(m - 1, n, count)
    else:
        return check(m, n - 1, count) + check(m - 1, n, count)


def check_dynamic(deep, weight, array):
    for i in range(deep):
        for j in range(weight):
            if array[i][j] == 0:
                if i == 0 and j == 0:
                    array[i][j] = 1
                elif i == 0:
                    array[i][j] = array[i][j - 1]
                elif j == 0:
                    array[i][j] = array[i - 1][j]
                else:
                    array[i][j] = array[i][j - 1] + array[i - 1][j]
    # print_map(deep, weight, array)
    return array[deep-1][weight-1]


if __name__ == '__main__':
    # m, n = map(lambda i: int(i), input().split())
    m, n = 3, 4
    arr = [[0 for _ in range(n)] for _ in range(m)]
    # print_map(m, n)
    print(check_dynamic(m, n, arr))
