def run():
    n, m = [int(i) for i in input().split()]
    coasts = []
    for _ in range(n):
        coasts.append([int(i) for i in input().split()])
    res = []
    for i in range(n):
        line = []
        for j in range(m):
            if i == 0 and j == 0:
                act_cost = coasts[i][j]
            elif i == 0:
                act_cost = coasts[i][j] + line[j - 1]
            elif j == 0:
                act_cost = coasts[i][j] + res[i - 1][j]
            else:
                act_cost = coasts[i][j] + max(line[j - 1], res[i - 1][j])
            line.append(act_cost)
        res.append(line)
    print(res[n - 1][m - 1])
    i = n - 1
    j = m - 1
    route = []
    while i != 0 or j != 0:
        if i == 0:
            route.append('R')
            j -= 1
            continue
        if j == 0:
            route.append('D')
            i -= 1
            continue
        if res[i][j - 1] > res[i - 1][j]:
            route.append('R')
            j -= 1
        elif res[i][j - 1] < res[i - 1][j]:
            route.append('D')
            i -= 1
        else:
            route.append('D')
            i -= 1
    route.reverse()
    print(' '.join(route))


if __name__ == '__main__':
    run()
