from random import random
import time


def find_sum(n, s):
    c = 0
    for i in range(0, len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == s:
                c += 1
                # return f'{n[i]} {n[j]}'
    return c


def find_sum_v2(n, s):
    c = 0
    n.sort()
    min = 0
    max = len(n) - 1
    while max > min:
        if n[min] + n[max] > s:
            max -= 1
        elif n[min] + n[max] < s:
            min += 1
        else:
            max -= 1
            c += 1
            # return f'{n[min]} {n[max]}'
    return c


def find_sum_v3(n, s):
    # c = 0
    num_set = set()
    for n in numbers:
        if (s - n) in num_set:
            # c += 1
            return f'{n} {s-n}'
        else:
            num_set.add(n)
    return None


if __name__ == '__main__':
    # count = 10000000
    # numbers = [int((random() * 2 - 1) * 10000) for _ in range(0, count)]
    # k = int(random() * 1000)
    count = int(input())
    numbers = list(map(lambda i: int(i), input().split()))
    k = int(input())
    # print(numbers)
    # start_time = time.time()
    print(find_sum_v3(numbers, k))
    # print(time.time() - start_time)
