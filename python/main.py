if __name__ == '__main__':
    a = set((1, 2, 3))
    b = set((4, 5, 6))
    c = a.union(b)
    d = set((1, 6))
    e = c.difference(d)

    print(b.union(d))
    print(b)
