def run(empls=None):
    if empls is None:
        empls = [int(i) for i in input().split()]
    gifts = {}

    for i in range(1, len(empls) + 1):
        gifts[i] = []
    for i, v in enumerate(empls):
        gifts[v].append(i + 1)

    self_p = two_p = no_p = 0

    for k in gifts.keys():
        g_num = len(gifts[k])
        if g_num == 0:
            if no_p == 0:
                no_p = k
            else:
                return -1, -1
        elif g_num == 2:
            if two_p == 0:
                two_p = k
            else:
                return -1, -1
        elif g_num == 1:
            pass
        else:
            return -1, -1
        if k in gifts[k]:
            if self_p == 0:
                self_p = k
            else:
                return -1, -1

    if no_p != 0:
        if self_p != 0 and two_p != 0 and self_p == two_p:
            if gifts[two_p][0] == two_p:
                a = gifts[two_p][0]
            else:
                a = gifts[two_p][1]
            new_empls = empls.copy()
            new_empls[a - 1] = no_p
            if check(new_empls):
                return a, no_p
        elif self_p == 0 and two_p != 0:
            if gifts[two_p][0] == no_p:
                a = gifts[two_p][1]
            else:
                a = gifts[two_p][0]
            new_empls = empls.copy()
            new_empls[a - 1] = no_p
            if check(new_empls):
                return a, no_p
    return -1, -1


def gen4(nums):
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                for l in nums:
                    if len({i, j, k, l}) > 2:
                        res.append([i, j, k, l])
    return res


def gen5(nums):
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                for l in nums:
                    for m in nums:
                        if len({i, j, k, l, m}) > 3:
                            res.append([i, j, k, l, m])
    return res


def gen3(nums):
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                if len({i, j, k}) > 1:
                    res.append([i, j, k])
    return res


def check(nums):
    ln = len(nums)
    if len(set(nums)) != ln:
        return False
    i = 1
    for _ in range(ln):
        if i == nums[i - 1]:
            return False
        i = nums[i - 1]
    if i == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print('hello')
    # input()
    for nums in gen3([1, 2, 3]):
        a = run(nums)
        print(f'{nums} - {a[0]} {a[1]}')
        if a[0] != -1:
            nums[a[0] - 1] = a[1]
            ch = check(nums)
            print(f'{nums} - {ch}')
    # a = run()
    # print(f'{a[0]} {a[1]}')
