if __name__ == '__main__':
    count = int(input())
    numbers = list(map(lambda i: int(i), input().split()))
    k = int(input())
    # count = 9
    # numbers = [9, 3, 2, 0, 1, 5, 1, 0, 0]
    # k = 3

    res = []

    current_sum = sum(numbers[:k])

    for i in range(0, len(numbers) - k):
        res.append(str(current_sum / k))
        current_sum -= numbers[i]
        current_sum += numbers[i + k]
    res.append(str(current_sum / k))

    print(" ".join(res))
