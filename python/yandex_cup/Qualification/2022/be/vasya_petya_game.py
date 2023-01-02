PETYA = 'Petya'
VASYA = 'Vasya'
DRAW = 'Draw'


def run():
    # goal, count = [int(i) for i in input().split()]
    # cards = [int(i) for i in input().split()]
    goal, count = 4, 12
    cards = [5, 10, 15, 20, 3, 6, 9, 25, 30, 12, 21, 24]
    p_s = 0
    v_s = 0
    i = 0
    while p_s < goal and v_s < goal and i != len(cards):
        act = cards[i]
        i += 1
        if act % 3 == 0 and act % 5 != 0:
            p_s += 1
        elif act % 3 != 0 and act % 5 == 0:
            v_s += 1

    else:
        if p_s == goal or p_s > v_s:
            print(PETYA)
        elif v_s == goal or p_s < v_s:
            print(VASYA)
        else:
            print(DRAW)


if __name__ == '__main__':
    run()