import time

class Node:
    def __init__(self, value, left=None, right=None):
        self.create_time = 0
        if isinstance(value, str):
            self.value = value
            self.left = left
            self.right = right
        elif isinstance(value, list):
            self.value = value[0]
            self.left = left
            self.right = right
            self.fill(value[1:])

    def __str__(self):
        return f'{self.value}'

    def add(self, value):
        t = time.time()
        new_n = Node(value)
        act = self
        while True:
            if act.value > value:
                if act.left is None:
                    act.left = new_n
                    break
                act = act.left
            elif act.value < value:
                if act.right is None:
                    act.right = new_n
                    break
                act = act.right
            else:
                break
        self.create_time += time.time() - t

    def fill(self, ls):
        for v in ls:
            self.add(v)

    def go(self):
        res = ''
        res += self.value
        if self.left is not None:
            res += self.left.go()
        if self.right is not None:
            res += self.right.go()
        return res


def combinations(s='', ls=None, res=None):
    if ls is None:
        ls = []
    if res is None:
        res = []
    if len(ls) == 0:
        res.append(s)
        return res
    for i in ls:
        n = list(ls)
        n.remove(i)
        combinations(f'{s}{i}', n, res)
    return res


def get_dif_tree(n):
    # t1 = time.time()
    num_list = [i for i in range(1, n + 1)]
    comb_list = combinations(ls=num_list)
    print(len(comb_list))
    # t2 = time.time()
    dif_tree = set()
    t4 = 0
    t5 = 0
    for comb in comb_list:
        t1 = time.time()
        tree = Node(list(comb))
        t2 = time.time()
        dif_tree.add(tree.go())
        # t3 = time.time()
        t4 += t2 - t1
        t5 += tree.create_time
    # t3 = time.time()
    print(t4)
    print(t5)
    return dif_tree


def run():
    # n = int(input())
    n = 10

    print(len(get_dif_tree(n)))

    # n = 4
    # for i in range(2, 10):
    #     print(len(get_dif_tree(i)))


if __name__ == '__main__':
    run()
