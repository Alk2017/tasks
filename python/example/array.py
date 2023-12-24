if __name__ == '__main__':
    ls = [1, 2, 3, 7, 8]

    # print(ls[1:])
    # print(ls[2:])
    # print(ls[3:])
    # print(ls[:1])
    # print(ls[:2])
    # print(ls[:3])
    #
    # print([1,3,5] + [6, 8, 9])

    ls.remove(2)
    del ls[-1]
    print(ls)