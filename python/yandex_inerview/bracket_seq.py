def bracket_gen(n, cur, o, cl, res):
    if len(cur) == 2 * n:
        res.append(cur)
    else:
        if o < n:
            bracket_gen(n, cur + "(", o + 1, cl, res)
        if o > cl:
            bracket_gen(n, cur + ")", o, cl + 1, res)
    return res


if __name__ == '__main__':
    # n = int(input())
    n = 3
    print(bracket_gen(n, "", 0, 0, []))
