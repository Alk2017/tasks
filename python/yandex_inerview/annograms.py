def dict_from_string(s):
    d = dict()
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 0
    return d


def check_annogram(s1, s2):
    d1 = dict_from_string(s1)
    d2 = dict_from_string(s2)
    return d1 == d2


if __name__ == '__main__':
    line1 = input()
    line2 = input()
    if check_annogram(line1, line2):
        print(1)
    else:
        print(0)
