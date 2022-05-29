def toDict(ls):
    dict = {}
    for n in ls:
        if n in dict.keys():
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def run():
    found = int(input())
    if found == 1:
        print(2)
        return
    if found == 2:
        print(1)
        return
    ls = [1, 2]
    res = 0
    for _ in range(found-2):
        new_ls = []
        for i in range(len(ls)-1):
            new_ls.append(ls[i])
            if ls[i] + ls[i + 1] <= found:
                new_ls.append(ls[i] + ls[i + 1])
                if ls[i] + ls[i + 1] == found:
                    res += 2
        new_ls.append(ls[-1])
        ls = new_ls
        # print(ls)
    print(res)


if __name__ == '__main__':
    run()

# 1 5 4 7 3 8 5 7 2
# 176_5___4___7___3___8_13_5_12_7_9_2

# 1, 3, 2
# 1, 4, 3, 5, 2
# 1, 5, 4, 7, 3, 8, 5, 7, 2]
# 1, 6, 5, 9, 4, 11, 7, 10, 3, 11, 8, 13, 5, 12, 7, 9, 2
