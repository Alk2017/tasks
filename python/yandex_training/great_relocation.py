def run():
    count = int(input())
    ls = [(int(i), ind) for (ind, i) in enumerate(input().split())]
    stack = [ls[0]]
    res = [-1]*count

    # |              #
    # |          #   #
    # |    #     #   # #
    # |  # # #   # # # #
    # |# # # # # # # # # #
    # 1 2 3 2 1 4 2 5 3 1 -> -1 4 3 4 -1 6 9 8 9 -1

    for c in ls[1:]:
        while len(stack) > 0 and c[0] < stack[-1][0]:
            res[stack.pop()[1]] = c[1]
        stack.append(c)
    print(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    run()
