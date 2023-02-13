def pr_s_to_ls(s):
    res = set()
    for pg in s.split(','):
        if '-' in pg:
            s, f = [int(i) for i in pg.split('-')]
            res.update(range(s, f + 1))
        else:
            res.add(int(pg))
    return list(res)


def pr_ls_to_s(ls):
    res = list()
    i = 0
    s = len(ls)
    while i < s:
        f = i
        l = 0
        while i < s - 1 and ls[i + 1] - ls[i] == 1:
            i += 1
            l = i
        if l == 0:
            res.append(str(ls[f]))
        else:
            res.append(f'{ls[f]}-{ls[l]}')
        i += 1
    # print(res)
    return ','.join(res)


def run():
    for _ in range(int(input())):
        c = int(input())
        pr_s = input()
        pr_ls = pr_s_to_ls(pr_s)
        # print(pr_ls)
        pr_ls.sort()
        nd_pr = list()
        for i in range(1, c + 1):
            if i not in pr_ls:
                nd_pr.append(i)
        # print(nd_pr)
        print(pr_ls_to_s(nd_pr))


if __name__ == '__main__':
    run()