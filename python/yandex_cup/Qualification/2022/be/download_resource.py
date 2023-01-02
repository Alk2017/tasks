def run():
    file_in = open('input_resource.txt', 'r')
    s_c = int(file_in.readline())
    clusters = []
    for _ in range(s_c):
        s1, s2 = [int(i) for i in file_in.readline().split()]
        already = (False, set())
        for c in clusters:
            if s1 in c or s2 in c:
                if already[0]:
                    new_cl = already[1] | c
                    clusters[clusters.index(already[1])] = new_cl
                    already = (True, new_cl)
                    c.clear()
                else:
                    c.add(s1)
                    c.add(s2)
                    already = (True, c)
        if not already[0]:
            clusters.append({s1, s2})
    f_c = int(file_in.readline())
    for _ in range(f_c):
        s, _ = [int(i) for i in file_in.readline().split()]
        f_s = [int(i) for i in file_in.readline().split()]
        find_cl = set()
        for cl in clusters:
            if s in cl:
                find_cl = cl
        res = []
        for ser in f_s:
            if ser in find_cl:
                res.append(ser)
        print(f'{len(res)} {" ".join([str(i) for i in res])}')


if __name__ == '__main__':
    run()
