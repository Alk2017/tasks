def run():
    count = int(input())
    lines = []
    for _ in range(count):
        lines.append(input())
    short_lines = []
    for l in lines:
        comp_lines = list(lines)
        comp_lines.remove(l)
        l_size = len(l)
        if l_size <= 3:
            short_lines.append(l)
            comp_lines.remove(l)
            continue
        problem = False
        for c_l in comp_lines:
            if len(c_l) == l_size and l[:1] == c_l[:1] and l[-1:] == c_l[-1:]:
                problem = True
                if l_size - 2 <= 3:
                    short_lines.append(l)
                    continue
                else:
                    if l[:2] == c_l[:2] and l[2:] == c_l[2:]:
                        pass
                    else:
                        short_lines.append(f'{l[:2]}{l_size-4}{l[-2:]}')
        if not problem:
            short_lines.append(f'{l[0]}{l_size-2}{l[-1]}')
    print('\n'.join(short_lines))



if __name__ == '__main__':
    run()

    # 10
    # aaaa
    # abaa
    # abab
    # bbbb
    # baba
    # aaaaaaaaaaaaaaaaaaaa
    # abaaaaaaaaaaaaaaaaaa
    # bbbbbbbbbbbbbbbbbbbb
    # sjfdhlsakdjfhsald
    # sdfasdfsadfafdsfdd
    # aaaa
    # abaa
    # a2b
    # b2b
    # b2a
    # aa16aa
    # ab16aa
    # b18b
    # s15d
    # s16d