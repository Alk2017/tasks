import sys


def get_min_t(L, x1, v1, x2, v2):
    t_values = []
    c = (x1 + x2) / 2 % (L / 2)
    v = (v1 + v2) / 2
    if v > 0:
        c = L / 2 - c
        print(c)
    if not c:
        t_values.append(c)
    if v:
        print(v)
        t_values.append(c / abs(v))

    delta_x = x2 - x1
    if not delta_x:
        t_values.append(delta_x)
    delta_v = v2 - v1
    if delta_x * delta_v > 0:
        delta_x = L - abs(delta_x)
    if delta_v:
        t_values.append(abs(delta_x) / abs(delta_v))
    if t_values:
        print(t_values)
        return min(t_values)


# L, x1, v1, x2, v2 = map(int, input('L, x1, v1, x2, v2->').split())
# x1 = x1 % L
# x2 = x2 % L


def run():
    # print('start')
    # dist, kr_pos, kr_sp, an_pos, an_sp = [int(i) for i in input().split()]
    dist, kr_pos, kr_sp, an_pos, an_sp = 6, 3, 1, 1, 1
    # dist, kr_pos, kr_sp, an_pos, an_sp = 12, 8, 10, 5, 20
    # dist, kr_pos, kr_sp, an_pos, an_sp = 5, 0, 0, 1, 2
    # dist, kr_pos, kr_sp, an_pos, an_sp = 10, 7, -3, 1, 4
    # dist, kr_pos, kr_sp, an_pos, an_sp = 615143346, 79387687, -80123649, 306422480, -80123649
    # 2.4075923389360363
    # if kr_sp == 0 and an_sp == 0:
    #     if kr_pos == an_pos:
    #         print('YES')
    #         print('0')
    #     else:
    #         print('NO')
    #     return
    # max distance from/to start line
    half_dist = dist / 2
    # direction if to max - false, to start - true
    kr_dir = kr_pos >= half_dist
    an_dir = an_pos >= half_dist

    # we need to build function for our line 'y = ax + b'
    kr_a = kr_sp
    kr_b = kr_pos
    kr_t_s = 0
    kr_t_f = 0
    kr_ch = True
    an_a = an_sp
    an_b = an_pos
    an_t_s = -1
    an_t_f = 0
    an_ch = True

    if kr_dir:
        kr_a *= -1
        kr_b = half_dist - (kr_pos - half_dist)
    if an_dir:
        an_a *= -1
        an_b = half_dist - (an_pos - half_dist)
    x = 0
    while x < 5:
        x += 1
        # print(f'Y(kr) = {kr_a} * X + {kr_b}')
        # print(f'Y(an) = {an_a} * X + {an_b}')
        x_dif = kr_a - an_a
        n_dif = an_b - kr_b
        if x_dif != 0:
            T = n_dif / x_dif
            if kr_ch:
                kr_t_s = kr_t_f
                if kr_a == 0:
                    kr_t_f = sys.maxsize
                else:
                    if kr_a > 0:
                        kr_t_f = (half_dist - kr_b) / kr_a
                    else:
                        kr_t_f = -kr_b / kr_a
                kr_ch = False
            if an_ch:
                an_t_s = an_t_f
                if an_a == 0:
                    an_t_f = sys.maxsize
                else:
                    if an_a >= 0:
                        an_t_f = (half_dist - an_b) / an_a
                    else:
                        an_t_f = -an_b / an_a
                an_ch = False
            # print(f'T(kr) = [{kr_t_s},{kr_t_f}]')
            # print(f'T(an) = [{an_t_s},{an_t_f}]')
            if min(kr_t_f, an_t_f) >= T >= max(kr_t_s, an_t_s):
                print('YES')
                print(T)
                return
        else:
            if n_dif == 0:
                print('YES')
                print('0')
                return
            if kr_a == 0:
                if kr_b != an_b:
                    print('NO')
                    return
        if kr_a > 0 and an_a > 0:
            if half_dist - kr_b < half_dist - an_b:
                kr_a *= -1
                kr_b = half_dist - (kr_b - half_dist)
                kr_ch = True
            else:
                an_a *= -1
                an_b = half_dist - (an_b - half_dist)
                an_ch = True
        elif kr_a < 0 and an_a < 0:
            if kr_b < an_b:
                kr_a *= -1
                kr_b *= -1
                kr_ch = True
            else:
                an_a *= -1
                an_b *= -1
                an_ch = True
        elif kr_a > 0 > an_a:
            if half_dist - kr_b < an_b:
                kr_a *= -1
                kr_b = half_dist - (kr_b - half_dist)
                kr_ch = True
            else:
                an_a *= -1
                an_b *= -1
                an_ch = True
        elif kr_a < 0 < an_a:
            if half_dist - an_b < kr_b:
                an_a *= -1
                an_b = half_dist - (an_b - half_dist)
                an_ch = True
            else:
                kr_a *= -1
                kr_b *= -1
                kr_ch = True
        elif an_a == 0:
            if kr_a > 0:
                kr_b = half_dist - (kr_b - half_dist)
            else:
                kr_b *= -1
            kr_ch = True
            kr_a *= -1
        elif kr_a == 0:
            if an_a > 0:
                an_b = half_dist - (an_b - half_dist)
            else:
                an_b *= -1
            an_ch = True
            an_a *= -1


def run2():
    # L, x1, v1, x2, v2 = [int(i) for i in input().split()]
    # L, x1, v1, x2, v2 = 6, 3, 1, 1, 1
    L, x1, v1, x2, v2 = 12, 8, 10, 5, 20
    # L, x1, v1, x2, v2 = 5, 0, 0, 1, 2
    # L, x1, v1, x2, v2 = 10, 7, -3, 1, 4
    # L, x1, v1, x2, v2 = 615143346, 79387687, -80123649, 306422480, -80123649
    t = get_min_t(L, x1, v1, x2, v2)
    if t is None:
        print('NO2')
    else:
        print('YES2')
    print(t)


if __name__ == '__main__':
    run2()
