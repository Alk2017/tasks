def turn_off(res, k, comp, t=0, j=0):
    if j == len(res):
        return t
    else:
        comp[j] = 0
        t += 1
        s = res[j] - 1
        if comp[s] != 0:
            comp[s] += 1
            if comp[s] == k:
                return turn_off(res, k, comp, t, s)
        return turn_off(res, k, comp, t, get_next(comp))


def get_next(comp):
    for c in comp.keys():
        if comp[c] != 0:
            return c


def run():
    file_in = open('input_storage.txt', 'r')
    count = int(file_in.readline())
    for _ in range(count):
        n, k = [int(i) for i in file_in.readline().split()]
        res_com = [int(i) for i in file_in.readline().split()]
        comp = dict()
        for i in range(n):
            comp[i] = 1
        print(turn_off(res_com, k, comp))



if __name__ == '__main__':
    run()

