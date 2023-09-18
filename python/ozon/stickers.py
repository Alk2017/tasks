def run():
    or_line = list(input())
    for _ in range(int(input())):
        swap_set = input().split()
        start = int(swap_set[0]) - 1
        end = int(swap_set[1]) - 1
        l = swap_set[2]
        if start == end:
            or_line[start] = l
        else:
            j = 0
            for i in range(start, end + 1):
                or_line[i] = l[j]
                j += 1
    print(''.join(or_line))


if __name__ == '__main__':
    run()
