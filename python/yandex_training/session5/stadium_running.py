def run():
    print('start')
    #    L, K_P, K_S, A_P, A_S = [int(i) for I in input().split()]
    L, K_P, K_S, A_P, A_S = 6, 4, 1, 2, 1
    if K_S == 0 and A_S == 0:
        if K_P == A_P:
            print('YES')
            print('0')
        else:
            print('NO')
        return
    M = L / 2
    K_D = K_P >= M
    A_D = A_P >= M
    if K_D:
        K_S *= -1
        if K_P > M:
            K_P = M - (K_P-M)
    if A_D:
        A_S *= -1
        A_P = M - (A_P-M)
    print(f'{K_P}, {K_S}, {A_P}, {A_S}')
    X = K_S - A_S
    N = A_P - K_P
    T = abs(N / X)
    print(T)
    # if X != 0:



if __name__ == '__main__':
    run()
