def run():
    for _ in range(int(input())):
        c = int(input())
        nums = [int(i) for i in input().split()]
        max_s = 0
        s = 0
        ns = []
        for i, n in enumerate(nums):
            if len(ns) < 2:
                ns.append(n)
                s += 1
            else:
                if n in ns:
                    s += 1
                else:
                    max_s = max(s, max_s)
                    s = 0
                    if nums[i - 1] == ns[0]:
                        ns.remove(ns[1])
                    else:
                        ns.remove(ns[0])
                    j = i-1
                    while j > 0 or nums[j] in ns:
                        s += 1
                        j -= 1
                    ns.append(n)
                    s += 1
        else:
            max_s = max(s, max_s)
        print(max_s)


if __name__ == '__main__':
    run()