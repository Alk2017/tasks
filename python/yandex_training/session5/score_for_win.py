def run():
    s1_1, s2_1 = [int(i) for i in input().split(':')]
    s1_2, s2_2 = [int(i) for i in input().split(':')]
    fg = True if input() == '1' else False
    dif = (s2_1 + s2_2) - (s1_1 + s1_2)
    if dif < 0:
        a = 0
    elif dif == 0:
        if fg:
            if s1_2 > s2_1:
                a = 0
            else:
                a = 1
        else:
            if s1_1 > s2_2:
                a = 0
            else:
                a = 1
    elif dif > 0:
        if fg:
            if (s1_2 + dif) > s2_1:
                a = dif
            else:
                a = 1 + dif
        else:
            if s1_1 > s2_2:
                a = dif
            else:
                a = 1 + dif
    print(a)


if __name__ == '__main__':
    run()
