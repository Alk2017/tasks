def run():
    for _ in range(int(input())):
        input()
        d, w = [int(i) for i in input().split()]
        t = []
        for _ in range(d):
            t.append([int(i) for i in input().split()])
        n = int(input())
        com = [int(i) for i in input().split()]
        uniq_c = []
        for i, c in enumerate(com):
            if i == 0 or i > 0 and com[i - 1] != c:
                uniq_c.append(c)
        for c in uniq_c:
            t.sort(key=lambda x: x[c - 1])
        for s in t:
            print(' '.join([str(i) for i in s]))
        print()


if __name__ == '__main__':
    run()
