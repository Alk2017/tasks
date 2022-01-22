import time


def get_pr(n):
    lp = [0] * (n + 1)
    pr = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        for p in pr:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return pr


def form(number, pr):
    res = []
    if number in pr:
        print(number)
    else:
        for i in pr:
            while number % i == 0:
                number //= i
                res.append(i)
            else:
                if number == 1:
                    break
            if number in pr:
                res.append(number)
                break
        print(' '.join([str(n) for n in res]))


def form2(number):
    res = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            number //= i
            res.append(i)
        else:
            i += 1
    if number > 1:
        res.append(number)
    print(' '.join([str(n) for n in res]))


if __name__ == '__main__':
    a = [3, 5, 4]
    b = '2 4 6'

    print(int(b.replace(' ', '')))
    # number = int(input())
    # start_time = time.time()
    # pr = get_pr(number)
    # form2(number)
    # time_1 = time.time() - start_time
    # form(number, pr)
    # time_2 = time.time() - time_1
    # print(time_1)
    # print(time_2)
