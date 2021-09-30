BIG = list(range(ord("A"), ord("Z") + 1))
SMALL = list(range(ord("a"), ord("z") + 1))


def check_count(line):
    c = 0
    is_shift = False
    if len(line) < 3:
        for i, let in enumerate(line):
            is_big = ord(let) in BIG
            if is_big == is_shift:
                c += 1
            else:
                c += 2
    else:
        for i, let in enumerate(line[:-2]):
            if ord(let) == 32:
                c += 1
                continue
            is_big = ord(let) in BIG
            if is_big == is_shift or ord(let) == 32:
                c += 1
            else:
                if is_big:
                    if ord(line[i + 1]) in BIG + [32] and ord(line[i + 2]) in BIG:
                        c += 3
                        is_shift = True
                    else:
                        c += 2
                else:
                    if ord(line[i + 1]) in SMALL + [32] and ord(line[i + 2]) in SMALL:
                        c += 3
                        is_shift = False
                    else:
                        c += 2
        for i, let in enumerate(line[-2:]):
            is_big = ord(let) in BIG
            if is_big == is_shift or ord(let) == 32:
                c += 1
            else:
                c += 2
    return c


if __name__ == '__main__':
    line = input()
    print(check_count(line))
    # line = "HelLo WORld"
    # a = "hello"
    # print(ord("a"))
    # print(ord("z"))
    # print(ord("A"))
    # print(ord("Z"))
    # print(ord(" "))
    # print(a[:-1])
    # print(a[-1])
    # print(a[-2])
    # print(list(range(ord("A"), ord("Z") + 1)) + [32])
