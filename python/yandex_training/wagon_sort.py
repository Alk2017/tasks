def run():
    count = int(input())
    train = [int(i) for i in input().split()]
    stack = [train[0]]
    res = []
    for w in train[1:]:
        while len(stack) > 0 and w > stack[-1]:
            res.append(stack.pop())
        stack.append(w)
    while len(stack) > 0:
        res.append(stack.pop())
    for p in zip(res[:-1], res[1:]):
        if p[0] > p[1]:
            print('NO')
            break
    else:
        print('YES')


if __name__ == '__main__':
    run()
