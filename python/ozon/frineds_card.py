def run():
    count_f, cards = [int(i) for i in input().split()]
    fr_c = list(enumerate([int(i) for i in input().split()]))
    fr_c.sort(key=lambda j: j[1], reverse=True)
    res = [None] * count_f
    impos = False
    for s in fr_c:
        if s[1] < cards:
            res[s[0]] = cards
            cards -= 1
        else:
            impos = True
            break
    if not impos:
        print(' '.join([str(i) for i in res]))
    else:
        print(-1)


if __name__ == '__main__':
    a = [(1,2), (3,4)]
    for n,m in a:
        print(f'{n} -- {m}')
    run()