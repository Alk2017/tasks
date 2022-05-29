def run():
    count = int(input())
    l = 0
    l_max = 0
    for _ in range(count):
        if int(input()) == 1:
            l += 1
        else:
            l_max = max(l_max, l)
            l = 0
    l_max = max(l_max, l)
    print(l_max)


if __name__ == '__main__':
    run()
