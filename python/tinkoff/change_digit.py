def biggest(num):
    ar = []
    ar.append(num % 10)
    while num // 10 != 0:
        num //= 10
        ar.append(num % 10)
    res = []
    k = 1
    for i in ar:
        res.append((9 - i) * k)
        k *= 10
    return res


def run():
    l1 = int('1111'*4)
    l2 = int('1111'*2)
    print(l1//l2)
    size, count = map(lambda i: int(i), input().split())
    nums = [int(i) for i in input().split()]
    score = []
    for num in nums:
        score += biggest(num)
    score.sort()
    score.reverse()
    sum = 0
    i = 0
    while i < count and i < len(score):
        sum += score[i]
        i += 1
    print(sum)


if __name__ == '__main__':
    run()