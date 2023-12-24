# 1 1 1 1 1 -> 4
# 1 1 0 1 1 -> 2
# 2 2 1 2 2 -> 6
# 5 4 3 2 1 ->


def run():
    c = int(input())
    t = []
    for _ in range(c):
        t.append(int(input()))
    # m = min(t)
    res = 0
    # res += m * (c-1)
    # for i in range(c):
    #     t[i] -= m
    while sum(t) != 0:
        i = 0
        while i != c:
            while i != c and t[i] == 0:
                i += 1
            if i == c:
                break
            long = 0
            start = i
            minim = t[i]
            while i != c and t[i] != 0:
                long += 1
                minim = min(minim, t[i])
                # t[i] -= 1
                i += 1
            finish = i
            for j in range(start, finish):
                t[j] -= minim
            res += (long - 1) * minim
    print(res)


if __name__ == '__main__':
    run()