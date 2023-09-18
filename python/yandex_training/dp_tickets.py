def run():
    n = int(input())
    abc = []
    for _ in range(n):
        abc.append([int(i) for i in input().split()])
    dp = [abc[0][0]]
    # min(dp[i-1] + Ai, dp[i-2] + Bi-1, dp[i-3] + Ci-2)
    if len(abc) == 1:
        print(dp[0])
        return
    dp.append(min((dp[0] + abc[1][0]), abc[0][1]))
    if len(abc) == 2:
        print(dp[1])
        return
    dp.append(min((dp[1] + abc[2][0]), (dp[0] + abc[1][1]), abc[0][2]))
    if len(abc) == 3:
        print(dp[2])
        return
    for i in range(3, n):
        dp.append(min((dp[i - 1] + abc[i][0]), (dp[i - 2] + abc[i - 1][1]),
                      (dp[i-3] + abc[i - 2][2])))
    print(dp[-1])


if __name__ == '__main__':
    run()
