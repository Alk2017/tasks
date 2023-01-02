from collections import defaultdict

def run():
    count = int(input())
    for _ in range(count):
        c = input()
        tasks = [int(i) for i in input().split()]
        uniq_t = {}
        res = 'YES'
        if len(tasks) != len(set(tasks)):
            for i, t in enumerate(tasks):
                if t in uniq_t:
                    if tasks[i - 1] != t:
                        res = 'NO'
                else:
                    uniq_t.append(t)
        print(res)


def run2():
    count = int(input())
    for _ in range(count):
        c = input()
        ls = input().split()
        tasks = defaultdict(list)
        for i, v in enumerate(ls):
            tasks[v].append(i)
        res = 'YES'
        for k in tasks.keys():
            if len(tasks[k]) > 1:
                for p, n in enumerate(tasks[k]):
                    if p > 0 and n-1 != tasks[k][p-1]:
                        res = 'NO'
        print(res)


if __name__ == '__main__':
    run2()
