import sys


def main():
    n, m = [int(i) for i in input().split()]
    costs = []
    dp = []
    for _ in range(n):
        costs.append([int(i) for i in input().split()])
        dp.append([0] * m)
    dp[0][0] = costs[0][0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + costs[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + costs[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + costs[i][j]
    print(dp[-1][-1])
    i = n - 1
    j = m - 1
    res = []
    while i != 0 or j != 0:
        prev = dp[i][j] - costs[i][j]
        if prev == dp[i - 1][j]:
            res.append('D')
            i -= 1
        elif prev == dp[i][j - 1]:
            res.append('R')
            j -= 1
    res.reverse()
    print(' '.join(res))


if __name__ == '__main__':
    main()