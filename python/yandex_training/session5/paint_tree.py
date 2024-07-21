def run():
    p, v = [int(i) for i in input().split()]
    q, m = [int(i) for i in input().split()]

    if (p + v) < (m - q) or (m + q) < (p - v):
        return 2 + ((p + v) - (p - v)) + ((q + m) - (q - m))
    else:
        if (p - v) <= (q - m):
            a = p - v
        else:
            a = q - m

        if (p + v) >= (q + m):
            b = p + v
        else:
            b = q + m
        return 1 + b - a


if __name__ == '__main__':
    print(run())