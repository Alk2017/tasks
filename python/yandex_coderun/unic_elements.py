def run():
    for _ in range(int(input())):
        input()
        ls = [int(i) for i in input().split()]
        m = dict()
        for i in ls:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        s = 0
        for k in m.keys():
            d = int(m[k] / 3)
            s += (m[k] - d) * k
        print(s)

if __name__ == '__main__':
    run()