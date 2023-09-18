if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5]
    # with combining
    print(ls[:-1])
    print(ls[1:])
    print(list(zip(ls[:-1], ls[1:])))

    print(ls[::2])
    print(ls[1::2])
    print(list(zip(ls[::2], ls[1::2])))

