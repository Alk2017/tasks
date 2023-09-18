def get_min(dp, numb):
    div_3 = div_2 = 0
    if numb % 3 == 0:
        div_3 = numb // 3
    if numb % 2 == 0:
        div_2 = numb // 2
    minus_1 = numb - 1
    a1 = dp[div_3 - 1] if div_3 != 0 else (0, 400000)
    a2 = dp[div_2 - 1] if div_2 != 0 else (0, 400000)
    a3 = dp[minus_1 - 1]
    if a1[1] == min(a1[1], a2[1], a3[1]):
        return 3, a1[1] + 1
    if a2[1] == min(a1[1], a2[1], a3[1]):
        return 2, a2[1] + 1
    if a3[1] == min(a1[1], a2[1], a3[1]):
        return 1, a3[1] + 1


def run():
    n = int(input())
    dp = [(1, 0), (2, 1), (3, 1)]
    for i in range(4, n + 1):
        dp.append(get_min(dp, i))

    act = dp[n - 1]
    c = act[1]
    res = [n]
    j = n
    while act[1] != 0:
        if act[0] == 1:
            j -= 1
        elif act[0] == 2:
            j //= 2
        elif act[0] == 3:
            j //= 3
        act = dp[j - 1]
        res.append(j)

    print(c)
    res.reverse()
    print(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    run()