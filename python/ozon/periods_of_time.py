def check_period(p):
    if p[0] < 0 or p[0] > 23 or p[1] < 0 or p[1] > 59 or p[2] < 0 or p[2] > 59:
        return False
    else:
        return True


def period2_more(p1, p2, eq=False):
    if p2[0] > p1[0]:
        return True
    elif p2[0] == p1[0]:
        if p2[1] > p1[1]:
            return True
        elif p2[1] == p1[1]:
            if p2[2] > p1[2]:
                return True
            elif p2[2] == p1[2] and eq:
                return True
    return False


def checks_interf(p1, p2, periods):
    for ps in periods:
        p3, p4 = ps
        if period2_more(p1, p4):
            if period2_more(p3, p2):
                return False
    return True


def run():
    c_s = int(input())
    for _ in range(c_s):
        c_p = int(input())
        res = 'YES'
        periods = []
        for _ in range(c_p):
            if res == 'NO':
                input()
                continue
            p1, p2 = map(
                lambda i: [int(j) for j in i.split(':')],
                input().split('-')
            )
            if check_period(p1) and check_period(p2):
                if period2_more(p1, p2, True):
                    if checks_interf(p1, p2, periods):
                        periods.append((p1, p2))
                        continue
            res = 'NO'
        print(res)


if __name__ == '__main__':
    run()