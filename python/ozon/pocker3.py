# (2, 3', 4', 5', 6', 7', 8', 9', T', J', Q', K', A')-(S, C', D', H')

CARD_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
MATH = ['S', 'C', 'D', 'H']


def run():
    # t_n = '19'
    # file_in = open(f'tests/{t_n}', 'r')
    # file_in_a = open(f'tests/{t_n}.a', 'r')
    # for _ in range(int(input())):
    for _ in range(int(input())):
    # for _ in range(int(file_in.readline())):
        cards = sum([[f'{i}{j}' for i in CARD_ORDER] for j in MATH], [])
        # cards.remove('5S')
        hands = []
        for _ in range(int(input())):
        # for _ in range(int(file_in.readline())):
            h = sorted([i for i in input().split()],
            # h = sorted([i for i in file_in.readline().split()],
                       key=lambda k: CARD_ORDER.index(k[0][0]),
                       reverse=True)
            hands.append(h)
            cards.remove(h[0])
            cards.remove(h[1])
        my_hand = hands[0]
        other_hands = hands[1:]
        other_hands.sort(key=lambda k: CARD_ORDER.index(k[0][0]), reverse=True)
        other_cards = set([i[0] for i in sum(other_hands, [])])
        other_pars = list(map(lambda c: c[0][0],
                              filter(lambda h: (h[0][0] == h[1][0]),
                                     other_hands)))
        res = []
        if my_hand[0][0] == my_hand[1][0]:
            if len(other_pars) == 0:
                for c in cards:
                    if CARD_ORDER.index(c[0]) <= CARD_ORDER.index(
                            my_hand[0][0]) or c[0] not in other_cards:
                        res.append(c)
            else:
                if CARD_ORDER.index(my_hand[0][0]) >= CARD_ORDER.index(
                        other_pars[0]):
                    for c in cards:
                        if c[0] not in other_cards or c[0] == my_hand[0][
                            0] or (c[0] not in other_pars and CARD_ORDER.index(
                            my_hand[0][0]) >= CARD_ORDER.index(c[0])):
                            res.append(c)
                else:
                    for c in cards:
                        if c[0] == my_hand[0][0]:
                            res.append(c)
        else:
            if len(other_pars) == 0:
                if CARD_ORDER.index(my_hand[0][0]) >= CARD_ORDER.index(
                        other_hands[0][0][0]):
                    for c in cards:
                        if c[0] not in other_cards or c[0] == my_hand[0][0] or \
                                c[0] == my_hand[1][0]:
                            res.append(c)
                else:
                    for c in cards:
                        if c[0] == my_hand[0][0] or c[0] == my_hand[1][
                            0] or CARD_ORDER.index(c[0]) > CARD_ORDER.index(
                            other_hands[0][0][0]):
                            res.append(c)
            else:
                if CARD_ORDER.index(my_hand[0][0]) >= CARD_ORDER.index(
                        other_pars[0]):
                    for c in cards:
                        if (c[0] == my_hand[0][0] or c[0] == my_hand[1][0]) and \
                                c[0] not in other_pars and CARD_ORDER.index(
                            c[0]) >= CARD_ORDER.index(other_pars[0]):
                            res.append(c)
        # res.sort(key=lambda k: k[0])
        res.sort(key=lambda k: CARD_ORDER.index(k[0][0]))
        print(len(res))
        # l = file_in_a.readline()
        # assert len(res) == int(l), f'{len(res)} != {l}, my hand = {my_hand}'
        if len(res) != 0:
            print('\n'.join(res))
            # for c in res:
                # a = file_in_a.readline()
                # assert c in a, f'{c} != {a}'


if __name__ == '__main__':
    run()

# 1
# 2
# TS TC
# AD AH
