import time


def run():
    f_in = open("input.txt", "r")
    count = int(f_in.readline())
    # count = int(input())
    centers = []
    for _ in range(count):
        # sh = [int(i) for i in input().split()]
        sh = [int(i) for i in f_in.readline().split()]
        if sh[0] == 0:
            c = (sh[2], sh[3])
            if c not in centers:
                centers.append(c)
        elif sh[0] == 1:
            min_x = max_x = sh[1]
            min_y = max_y = sh[2]
            for j in range(3, 9):
                if j % 2 == 1:
                    min_x = min(sh[j], min_x)
                    max_x = max(sh[j], max_x)
                else:
                    min_y = min(sh[j], min_y)
                    max_y = max(sh[j], max_y)
            c = ((max_x + min_x) / 2, (max_y + min_y) / 2)
            if c not in centers:
                centers.append(c)
        else:
            print('Unknow shape')
    f_in.close()
    check(centers)


def check(c):
    if len(c) < 3:
        print('Yes')
        return
    x = c[0][0]
    swap = -1
    same_x = True
    for i, sh in enumerate(c):
        if sh[0] != x:
            swap = i
            same_x = False
            break
    if same_x:
        print('Yes')
        return
    if c[0][0] == c[1][0]:
        c[1], c[swap] = c[swap], c[1]
    a = (c[0][1] - c[1][1]) / (c[0][0] - c[1][0])
    b = c[0][1] - a * c[0][0]
    for sh in c:
        if sh[1] != sh[0] * a + b:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    run()
    # count = 100000
    # centers = []
    # for i in range(count):
    #     centers.append((i, i+1))
    # centers.append((-3, 3))
    # time1 = time.time()
    # check(centers)
    # print(time.time() - time1)
