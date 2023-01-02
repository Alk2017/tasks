def min_skill_dif(devs):
    skill = devs[0]
    min_dif = abs(skill - devs[1])
    min_skill = devs[1]
    for other_s in devs[1:]:
        dif = abs(skill - other_s)
        if dif == 0:
            return other_s
        if dif < min_dif:
            min_dif = dif
            min_skill = other_s
    return min_skill


def run():
    count = int(input())
    couples = []
    for _ in range(count):
        c = input()
        devs = [int(i) for i in input().split()]
        act_min = min_skill_dif(devs)
        order = len(couples) * 2 + 1
        couples.append(f'{order} {devs.index(act_min) + order}')
        devs.remove(devs[0])
        devs.re

if __name__ == '__main__':
    # run()
    assert min_skill_dif([2, 1, 3, 1, 1, 4]) == 1
    assert min_skill_dif([3, 1, 1, 4]) == 4

"""
2 1 3 1 1 4

2 1

3 4

1 1


"""
