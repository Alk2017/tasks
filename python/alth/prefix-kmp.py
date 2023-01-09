import time
from random import random


def max_prefix(s):
    t = time.time()
    n = len(s)
    Pi = [0 for _ in range(n)]
    for i in range(1, n):
        p = Pi[i-1]
        while p > 0 and s[i] != s[p]:
            p = Pi[p-1]
        if s[i] == s[p]:
            p += 1
        Pi[i] = p
    print(time.time() - t)
    print(max(Pi))


def run():
    # print(max_prefix(a))
    count = 5000000
    times = 10
    for _ in range(times):
        random_ch_list = [chr(int(random() * 26 + 97)) for _ in range(0, count)]
        random_ch_list.insert(count//5, '#')
        random_str = ''.join(random_ch_list)
        max_prefix(random_str)

if __name__ == "__main__":
    run()