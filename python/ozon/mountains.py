def prin(p):
    for i in range(len(p)):
        print(''.join(p[i]))
    print('')


def run():
    for _ in range(int(input())):
        c, n, m = [int(i) for i in input().split()]
        pic = []
        for _ in range(n):
            pic.append(list(input()))
        for _ in range(1, c):
            input()
            s_pic = []
            for _ in range(n):
                s_pic.append(list(input()))
            for i in range(n):
                for j in range(m):
                    if s_pic[i][j] != '.' and pic[i][j] == '.':
                        pic[i][j] = s_pic[i][j]
        prin(pic)


if __name__ == '__main__':
    run()