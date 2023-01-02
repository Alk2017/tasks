DISABLE = 'DISABLE'
RESET = 'RESET'
GETMAX = 'GETMAX'
GETMIN = 'GETMIN'


def get_max(cl):
    max_v = cl[0][-1] * cl[0][-2]
    max_i = 0
    for i in range(1, len(cl)):
        if max_v < cl[i][-1] * cl[i][-2]:
            max_i = i
    return max_i + 1


def get_min(cl):
    min_v = cl[0][-1] * cl[0][-2]
    min_i = 0
    for i in range(1, len(cl)):
        if min_v > cl[i][-1] * cl[i][-2]:
            min_i = i
    return min_i + 1


def run():
    file_in = open('input_reset.txt', 'r')
    c_dc, c_s, c_a = [int(i) for i in file_in.readline().split()]
    cluster = [[True] * c_s + [0, c_s]] * c_dc
    for _ in range(c_a):
        cms = file_in.readline().split()
        if cms[0] == DISABLE:
            dc = int(cms[1])
            s = int(cms[2])
            if cluster[dc - 1][s - 1]:
                cluster[dc - 1][s - 1] = False
                cluster[dc - 1][-1] -= 1
        elif cms[0] == RESET:
            dc = int(cms[1])
            res_c = cluster[dc - 1][-2]
            cluster[dc - 1] = [True] * c_s + [res_c + 1, c_s]
        elif cms[0] == GETMAX:
            print(get_max(cluster))
        elif cms[0] == GETMIN:
            print(get_min(cluster))
        else:
            print('ERROR COMAND')


if __name__ == '__main__':
    run()
    # https://contest.yandex.ru/yacup/contest/42202/problems/A/