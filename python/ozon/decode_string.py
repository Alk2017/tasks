def run():
    dec = {'00': 'a', '100': 'b', '101': 'c', '11': 'd'}
    c = int(input())
    for _ in range(c):
        c_s = input()
        res = ''
        i = 0
        while i != len(c_s):
            for k in dec.keys():
                if c_s.find(k, i) == i:
                    res += dec[k]
                    i += len(k)
        else:
            print(res)


if __name__ == '__main__':
    run()