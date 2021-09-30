ONE = 'one'
ZERO = 'zero'
O = 'o'
Z = 'z'


def check_count_number(line):
    return line.count(ONE) + line.count(ZERO)


def compare_lines(str1, str2):
    i1 = 0
    i2 = 0
    while str1[i1] == str2[i2]:
        if str1[i1] == O:
            i1 += 3
        else:
            i1 += 4
        if str2[i2] == O:
            i2 += 3
        else:
            i2 += 4

    if str1[i1] == O:
        print('>')
    else:
        print('<')


if __name__ == '__main__':
    line1 = input()
    line2 = input()
    count_line1 = check_count_number(line1)
    count_line2 = check_count_number(line2)
    if line1 == line2:
        print('=')
    elif count_line1 > count_line2:
        print('>')
    elif count_line1 < count_line2:
        print('<')
    else:
        compare_lines(line1, line2)
