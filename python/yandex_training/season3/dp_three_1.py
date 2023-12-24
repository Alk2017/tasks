def run():
    n = int(input())
    dp = [0] * max(3, n)
    dp[0] = 2 # 0,1
    dp[1] = 4 # 00, 01, 10, 11
    dp[2] = 7 # 000, 001, 010, 011, 100, 101, 110, 111

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n-1])


if __name__ == '__main__':
    run()

