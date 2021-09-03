def div_and_round_up(num, cut_count):
    if num % cut_count == 0:
        return num // cut_count
    else:
        return num // cut_count + 1


if __name__ == '__main__':
    count, cut = map(lambda i: int(i), input().split())
    logs = list(map(lambda i: int(i), input().split()))
    logs.sort()
    if cut == 0:
        print(logs[-1])
    elif cut == 1:
        print(div_and_round_up(logs[-1], cut))
    else:
        max_log = logs[-1]
        logs.remove(max_log)
        next_max = logs[-1]
        while cut > 0:
            k = max_log // next_max
            if k >= 2:
                logs.append(div_and_round_up(max_log, k))

            if next_max <= max_log // 2:
                cut -= 1





