if __name__ == '__main__':
    p, count = map(lambda i: int(i), input().split())
    villages = list(map(lambda i: int(i), input().split()))
    res = []
    previous_village = 0
    for v in villages:
        if len(res) == 0:
            res.append(villages[0] + p - villages[-1])
        else:
            res.append(v - previous_village)
        previous_village = v
    print(p - max(res))
