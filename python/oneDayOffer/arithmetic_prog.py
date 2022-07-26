from random import randint
import time


class MyProg2:
    def __init__(self):
        self.progs = {}

    def add(self, p):
        self.progs[p[2]] = p[:2]

    def remove(self, id):
        self.progs.pop(id)

    def min(self):
        ids = list(self.progs.keys())
        ids.sort(key=lambda id: self.progs[id])
        old = self.progs[ids[0]][0]
        self.progs[ids[0]][0] += self.progs[ids[0]][1]
        return old


class MyProg:

    def __init__(self):
        self.progs = {}
        self.mins = []

    def add(self, p):
        self.progs[p[2]] = p[:2]
        self.mins.append(p[2])
        self.mins.sort(key=lambda id: self.progs[id])

    def remove(self, id):
        self.progs.pop(id)
        self.mins.remove(id)

    def min(self):
        if len(self.progs) == 0:
            return 'empty'
        old = self.progs[self.mins[0]][0]
        self.progs[self.mins[0]][0] += self.progs[self.mins[0]][1]
        if len(self.mins) > 1 and (
                self.progs[self.mins[0]][0] > self.progs[self.mins[1]][0] or (
                self.progs[self.mins[0]][0] == self.progs[self.mins[1]][0] and
                self.progs[self.mins[0]][1] > self.progs[self.mins[1]][1])):
            self.mins.sort(key=lambda id: self.progs[id])
        return f'{old}\n'


def run(data=None):
    # file_in = open('input.txt', 'r')
    # file_out = open('output.txt', 'a')
    pr = MyProg()
    count = int(input()) if data is None else len(data)
    # count = int(file_in.readline())
    for i in range(count):
        d = input() if data is None else data[i]
        # d = file_in.readline()
        cmds = [int(i) for i in d.split()]
        if cmds[0] == 1:
            pr.add(cmds[1:])
        elif cmds[0] == 2:
            pr.remove(cmds[1])
        elif cmds[0] == 3:
            # file_out.write(pr.min())
            # pr.min()
            print(pr.min())
        else:
            print(f'unknown operation: {cmds[0]}')
    # file_in.close()
    # file_out.close()


def gen(count):
    res = []
    id_inc = 0
    for i in range(count):
        op_type = randint(1, 3)
        first_el = randint(-10 ** 9, 10 ** 9)
        delta = randint(-10 ** 9, 10 ** 9)
        if op_type == 1:
            id_inc += 1
            res.append(f'{op_type} {first_el} {delta} {id_inc}')
        elif op_type == 2:
            if id_inc > 0:
                res.append(f'{op_type} {id_inc}')
                id_inc -= 1
            else:
                id_inc += 1
                res.append(f'1 {first_el} {delta} {id_inc}')
        elif op_type == 3:
            if id_inc > 0:
                res.append(f'{op_type}')
            else:
                id_inc += 1
                res.append(f'1 {first_el} {delta} {id_inc}')
        else:
            print('error: unknown type')
    return res


if __name__ == '__main__':
    # run()
    for _ in range(100):
        data = gen(100000)
        # print('Data:')
        # print('\n'.join(data))
        # print('=========')
        start_time = time.time()
        run(data)
        print(f'Time: {time.time() - start_time}')
