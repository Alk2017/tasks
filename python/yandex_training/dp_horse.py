def run():
    n, m = [int(i) for i in input().split()]
    res = [[1] + [0] * (m - 1), [0] * 2 + [1] + [0] * (m - 3),
           [0] + [1] + [0] * (m - 2)]
    for i in range(3, n):
        line = []
        for j in range(m):
            pass
            # if i == 0 and j == 0:
            #     line.append(coasts[i][j])
            # elif i == 0:
            #     line.append(coasts[i][j] + line[j - 1])
            # elif j == 0:
            #     line.append(coasts[i][j] + res[i - 1][j])
            # else:
            #     line.append(coasts[i][j] + min(line[j - 1], res[i - 1][j]))
        res.append(line)
    print(res[n - 1][m - 1])


if __name__ == '__main__':
    run()
