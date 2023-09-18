def run():
    n = int(input())
    pins = [int(i) for i in input().split()]
    pins.sort()
    dp = [0] * n
    dp[1] = pins[1] - pins[0]
    if len(pins) == 2:
        print(dp[1])
        return
    dp[2] = dp[1] + pins[2] - pins[1]
    for j in range(3, n):
        dif = pins[j] - pins[j - 1]
        dp[j] = min(dp[j - 1] + dif, dp[j - 2] + dif)
    print(dp[n - 1])


if __name__ == '__main__':
    run()
