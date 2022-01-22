def check_subsequence(nums):
    max_sub = 0
    left = 0
    right = 0
    d = dict()
    for i in range(0, len(nums)):
        cur = nums[i]
        if cur in d:
            # d = dict()
            left = max(d[cur] + 1, left)
            d[cur] = i
        else:
            d[cur] = i
        right = i
        max_sub = max(max_sub, right - left + 1)
    return max_sub


if __name__ == '__main__':
    # line = list(map(lambda i: int(i), input().split()))
    ex = [
        "1 1",
        "1 2 3 4 5 5",
        "1 2 3 1 4",
        "1 2 3 3 2 1 5",
        "1 2 3 4 5 4 5 5 4 1"
    ]
    an = [
        1,
        5,
        4,
        4,
        5
    ]
    for i in range(0, len(ex)):
        a = check_subsequence(
            list(map(lambda i: int(i), ex[i].split()))
        )
        print(a)
        assert check_subsequence(
            list(map(lambda i: int(i), ex[i].split()))
        ) == an[i]
