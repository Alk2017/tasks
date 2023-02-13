def getPossFr(p1, vk):
    poss = set()
    if p1 not in vk.keys():
        return poss
    for fr in vk[p1]:
        poss = poss.union(vk[fr].difference(vk[p1].union({p1})))
    return poss


def getCommon(f1, f2, vk):
    s1 = vk[f1]
    s2 = vk[f2]
    return len(s1.intersection(s2))


def run():
    n, m = [int(i) for i in input().split()]
    vk = dict()
    for _ in range(m):
        f1, f2 = [int(i) for i in input().split()]
        if f1 in vk:
            vk[f1].add(f2)
        else:
            vk[f1] = {f2}
        if f2 in vk:
            vk[f2].add(f1)
        else:
            vk[f2] = {f1}
    for p in range(1, n+1):
        poss_fr = getPossFr(p, vk)
        if len(poss_fr) == 0:
            print('0')
        elif len(poss_fr) == 1:
            print(poss_fr.pop())
        else:
            res = []
            max_fr = 0
            for fr in poss_fr:
                c = getCommon(p, fr, vk)
                if c > max_fr:
                    res = [fr]
                    max_fr = c
                elif c == max_fr:
                    res.append(fr)
            if len(res) == 1:
                print(res[0])
                continue
            res.sort()
            print(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    run()