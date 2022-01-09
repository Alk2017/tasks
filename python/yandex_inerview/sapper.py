def create_field(x, y, bomb_list):
    res = []
    for n in range(0, y):
        line = []
        for m in range(0, x):
            if (n, m) in bomb_list:
                line.append(1)
            else:
                line.append(0)
        res.append(line)
    return res


def find_group(dot, f, res):
    neighbors = find_neighbor(dot, f)
    for n in neighbors - res:
        res.add(n)
        find_group(n, f, res)
    else:
        return res


def find_group_stack(dot, f):
    res = {dot}
    stack = [dot]
    while len(stack) != 0:
        neighbors = find_neighbor(dot, f) - res
        if len(neighbors) == 0:
            stack.pop()
            if len(stack) > 0:
                dot = stack[-1]
        else:
            dot = neighbors.pop()
            res.add(dot)
            stack.append(dot)
    return res


def find_neighbor(dot, f):
    y = dot[0]
    x = dot[1]
    res = set()
    if x + 1 < len(f[y]) and f[y][x + 1] != 1:
        res.add((y, x + 1))
    if y + 1 < len(f) and f[y + 1][x] != 1:
        res.add((y + 1, x))
    if x - 1 >= 0 and f[y][x - 1] != 1:
        res.add((y, x - 1))
    if y - 1 >= 0 and f[y - 1][x] != 1:
        res.add((y - 1, x))
    return res


# def print_field(f):
#     print('  0 1 2')
#     for i in range(0, size_y):
#         print(f'{i}|', end='')
#         for j in range(0, size_x):
#             if f[i][j] == 1:
#                 print('*|', end='')
#             else:
#                 print(' |', end='')
#         print()


if __name__ == '__main__':
    size_y, size_x = map(lambda i: int(i), input().split())
    count_bomb = int(input())
    count_free = size_x * size_y - count_bomb
    free_set = set()
    click_count = 0
    bombs = []
    for _ in range(0, count_bomb):
        bombs.append(tuple(map(lambda i: int(i) - 1, input().split())))
    # add checking 0 and 1 free cells
    field = create_field(size_x, size_y, bombs)
    # print_field(field)
    for i in range(0, size_y):
        if len(free_set) == count_free:
            break
        for j in range(0, size_x):
            d = (i, j)
            if field[i][j] == 0 and d not in free_set:
                group = find_group_stack(d, field)
                free_set = free_set.union(group)
                click_count += 1
            if len(free_set) == count_free:
                break
    print(click_count)
