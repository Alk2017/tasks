def run():
    for _ in range(int(input())):
        st_r = [15, 30]
        impbl = False
        for _ in range(int(input())):
            i_set = input().split()
            if impbl:
                print('-1')
                continue
            t = int(i_set[1])
            if i_set[0] == '>=':
                if t <= st_r[0]:
                    print(st_r[0])
                elif t > st_r[1]:
                    print('-1')
                    impbl = True
                else:
                    st_r[0] = t
                    print(st_r[0])
            elif i_set[0] == '<=':
                if t >= st_r[1]:
                    print(st_r[1])
                elif t < st_r[0]:
                    print('-1')
                    impbl = True
                else:
                    st_r[1] = t
                    print(st_r[1])
            else:
                print('wrong sign')
                break
        print('')


if __name__ == '__main__':
    run()