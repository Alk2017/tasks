import sys
import time
from random import randrange


class Heap:
    def __init__(self):
        self.ls = []
        self.size = 0

    def __str__(self):
        return ', '.join([f'{i}:{v}' for i, v in enumerate(self.ls)])

    # next 2i+1, 2i+2
    # prev (i-1)//2

    def push(self, el):
        self.ls.append(el)
        self.size += 1
        if len(self.ls) != 1:
            self.__sift_up()

    def pop(self):
        if self.size == 0:
            return -1, -1
        else:
            self.ls[0], self.ls[-1] = self.ls[-1], self.ls[0]
            res = self.ls[-1]
            del self.ls[-1]
            self.size -= 1
            self.__sift_down()
            return res

    def __get_prev(self, i):
        if i == 0:
            return -1, -1
        else:
            prev_i = (i - 1) // 2
            return prev_i, self.ls[prev_i]

    def __get_ch(self, i, right=False):
        ch_i = 2 * i
        if right:
            ch_i += 2
        else:
            ch_i += 1

        if ch_i >= self.size:
            return -1, -1
        else:
            return ch_i, self.ls[ch_i]

    def __get_ch_min(self, i):
        ch_i_l = 2 * i + 1
        ch_i_r = 2 * i + 2

        if ch_i_l >= self.size:
            return -1, -1
        elif ch_i_r >= self.size or self.ls[ch_i_r] >= self.ls[ch_i_l]:
            return ch_i_l, self.ls[ch_i_l]
        else:
            return ch_i_r, self.ls[ch_i_r]

    def __sift_up(self):
        act_i = self.size - 1
        prev_i, prev_v = self.__get_prev(act_i)
        while act_i != 0 and prev_i != -1:
            if self.ls[act_i][0] < prev_v[0]:
                self.ls[prev_i], self.ls[act_i] = self.ls[act_i], self.ls[
                    prev_i]
                act_i = prev_i
                prev_i, prev_v = self.__get_prev(act_i)
            else:
                break

    def __sift_down(self):
        act_i = 0
        ch_i, ch_v = self.__get_ch_min(act_i)
        while ch_i != -1:
            if self.ls[act_i][0] > ch_v[0]:
                self.ls[act_i], self.ls[ch_i] = self.ls[ch_i], self.ls[act_i]
                act_i = ch_i
            else:
                break
            ch_i, ch_v = self.__get_ch_min(act_i)


def get_min_i(ls_i, ls_el):
    d = len(ls_i)
    if d == 0:
        return -1
    i_m = -1
    m = sys.maxsize
    for j in range(d):
        if ls_i[j] != -1 and ls_el[j][ls_i[j]] < m:
            m = ls_el[j][ls_i[j]]
            i_m = j
    return i_m, m


def merge_line(ls):
    d = len(ls)
    res = []
    if d == 0:
        return res
    w = len(ls[0])
    ls_i = [0] * d
    while len(res) < d * w:
        m_i, m = get_min_i(ls_i, ls)
        res.append(m)
        if ls_i[m_i] == w - 1:
            ls_i[m_i] = -1
        else:
            ls_i[m_i] += 1
    return res


def merge_line2(ls):
    d = len(ls)
    res = []
    if d == 0:
        return res
    w = len(ls[0])
    ls_i = [0] * d
    h = Heap()
    for i, l in enumerate(ls):
        h.push((l[0], i))
    while len(res) < d * w:
        min_el = h.pop()
        res.append(min_el[0])
        if ls_i[min_el[1]] != w - 1:
            ls_i[min_el[1]] += 1
            h.push((ls[min_el[1]][ls_i[min_el[1]]], min_el[1]))
    return res


def run():
    n = 1000
    a = [sorted([randrange(100) for _ in range(n)]) for _ in range(n)]
    # start_time = time.time()
    # merge_line(a)
    # print(time.time() - start_time)
    start_time = time.time()
    merge_line2(a)
    print(time.time() - start_time)
    # ls = [
    #     [1, 5, 6, 8],
    #     [2, 4, 5, 9],
    #     [1, 4, 6, 7],
    #     [3, 4, 9, 17]
    # ]
    # print(merge_line2(ls))


if __name__ == '__main__':
    run()
