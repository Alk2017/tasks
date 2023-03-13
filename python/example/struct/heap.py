class MyHeap:
    def __init__(self):
        self.ls = []

    def insert(self, v):
        self.ls.append(v)
        act_i = len(self.ls) - 1
        if act_i == 0:
            return
        parent_i = (act_i - 1) // 2
        while self.ls[parent_i] < self.ls[act_i]:
            self.__swap(parent_i, act_i)
            act_i = parent_i
            if act_i == 0:
                return
            parent_i = (act_i - 1) // 2

    def extract(self):
        print(self.ls[0])
        last_i = len(self.ls) - 1
        if last_i == 0:
            self.ls.clear()
            return
        self.__swap(0, last_i)
        self.ls.pop(last_i)
        if len(self.ls) == 1:
            return
        act_i = 0
        max_ch_i = self.__get_max_ch(act_i)
        while self.ls[act_i] < self.ls[max_ch_i] and max_ch_i != -1:
            self.__swap(act_i, max_ch_i)
            act_i = max_ch_i
            max_ch_i = self.__get_max_ch(act_i)

    def __get_max_ch(self, i):
        last_i = len(self.ls) - 1
        lf_ch_i = 2 * i + 1
        rt_ch_i = 2 * i + 2
        if last_i < lf_ch_i:
            return -1
        elif last_i == lf_ch_i:
            return lf_ch_i
        elif self.ls[lf_ch_i] > self.ls[rt_ch_i]:
            return lf_ch_i
        else:
            return rt_ch_i

    def __swap(self, i1, i2):
        self.ls[i1], self.ls[i2] = self.ls[i2], self.ls[i1]
