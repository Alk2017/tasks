def rem(index, skill, sort_ls, dict_ls):
    dict_ls[skill].remove(index)
    if len(dict_ls[skill]) == 0:
        del dict_ls[skill]
        sort_ls.remove(skill)


def run():
    count = int(input())
    # count = 1
    for _ in range(count):
        res = []
        c = input()
        # ls = [int(i) for i in '3 4 5 4 2 5'.split()]
        ls = [int(i) for i in input().split()]
        sort_ls = list(set(ls))
        sort_ls.sort()
        d_ls = dict()
        for i, s in enumerate(ls):
            if s in d_ls.keys():
                d_ls[s].append(i)
            else:
                d_ls[s] = [i]
        #######################################
        i = 0
        while len(sort_ls) != 0:
            if i in res:
                i += 1
                continue
            skill = ls[i]
            #     Choose near skill pair
            if len(d_ls[skill]) > 1:
                p_s = skill
            elif skill == sort_ls[0]:
                p_s = sort_ls[1]
            elif skill == sort_ls[-1]:
                p_s = sort_ls[-2]
            else:
                act_i = sort_ls.index(skill)
                if sort_ls[act_i] - sort_ls[act_i - 1] < \
                        (sort_ls[act_i + 1] - sort_ls[act_i]):
                    p_s = sort_ls[act_i - 1]
                elif sort_ls[act_i] - sort_ls[act_i - 1] > \
                        (sort_ls[act_i + 1] - sort_ls[act_i]):
                    p_s = sort_ls[act_i + 1]
                else:
                    if d_ls[sort_ls[act_i + 1]][0] < \
                            (d_ls[sort_ls[act_i - 1]][0]):
                        p_s = sort_ls[act_i + 1]
                    else:
                        p_s = sort_ls[act_i - 1]
            res.append(i)
            rem(i, skill, sort_ls, d_ls)
            p_i = d_ls[p_s][0]
            res.append(p_i)
            rem(p_i, p_s, sort_ls, d_ls)
        print('\n'.join([f'{j[0] + 1} {j[1] + 1}' for j in
                         list(zip(res[::2], res[1::2]))]))
        print('')


if __name__ == '__main__':
    run()
    # assert min_skill_dif([2, 1, 3, 1, 1, 4]) == 1
