def line_to_dict(d, l):
    for ch in l:
        n = ord(ch)
        if n < 33 or n > 126:
            continue
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1


def run():
    ch_dict = dict()
    for line in open('input.txt', 'r'):
        line_to_dict(ch_dict, line)
    # line = input()
    # while len(line) != 0:
    #     line_to_dict(ch_dict, line)
    #     line = input()
    #     try:
    #         line = input()
    #     except EOFError:
    #         break
    chs = list(ch_dict.keys())
    chs.sort()
    if len(ch_dict.values()) == 0:
        return
    max_c = max(ch_dict.values())
    for c in range(max_c, 0, -1):
        res_line = ''
        for ch in chs:
            if ch_dict[ch] >= c:
                res_line += '#'
            else:
                res_line += ' '
        print(res_line, end='\n')
    print(''.join([chr(i) for i in chs]))


if __name__ == '__main__':
    # for i in range(128):
    #     print(f'{i} - {chr(i)}')
    run()