def run():
    for _ in range(int(input())):
        input()
        n, m = [int(i) for i in input().split()]
        tb = []
        for _ in range(n):
            tb.append([int(l) for l in input().split()])
        input()
        for click_i in [(int(i) - 1) for i in input().split()]:
            tb.sort(key=lambda r: r[click_i])

        for r in range(n):
            print(' '.join([str(n) for n in tb[r]]))
        print('')


if __name__ == '__main__':
    run()