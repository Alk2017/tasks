def run():
    M = int(input())
    N = int(input())
    old = []
    new = []
    for _ in range(N):
        s, f = [int(i) for i in input().split()]
        new.append((s, f))
        # if s == 5050226 or s == 5050221:
        #     print('')
        for ch in old:
            if ch[1] >= s >= ch[0] or ch[1] >= f >= ch[0] or s <= ch[0] <= ch[1] <= f:
                continue
            new.append(ch)
        old = new
        new = []
    print(len(old))


def run1():
    file_in = open('input.txt', 'r')
    M = int(file_in.readline())
    N = int(file_in.readline())
    res = [0]*M
    for _ in range(N):
        s, f = [int(i) for i in file_in.readline().split()]
        for i in range(s, f):
            res[i] += 1
    file_in.close()
    file_out = open('output.txt', 'a')
    for i in range(M):
        file_out.write(f'{i} - {res[i]}\n')
    file_out.close()


if __name__ == '__main__':
    run()
    # run1()