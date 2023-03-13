class MyRingBuff:
    def __init__(self, cap):
        self.cap = cap
        self.buf = [None] * cap
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        self.buf[self.tail] = item
        self.tail += 1
        self.tail %= self.cap
        if self.size < self.cap:
            self.size += 1
        else:
            self.head += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.head += 1
            self.head %= self.cap
            self.size -= 1
            return self.buf[self.head - 1]

    def qu_size(self):
        return self.size


def run():
    pl1 = MyRingBuff(10)
    pl2 = MyRingBuff(10)
    # map(lambda card: pl1.push(int(card)), input().split())
    # map(lambda card: pl2.push(int(card)), input().split())
    for card in input().split():
        pl1.push(int(card))
    for card in input().split():
        pl2.push(int(card))
    round = 0
    while pl1.size != 0 and pl2.size != 0:
        cr1 = pl1.pop()
        cr2 = pl2.pop()
        if cr1 == 0 and cr2 == 9:
            winner = pl1
        elif cr2 == 0 and cr1 == 9:
            winner = pl2
        elif cr1 > cr2:
            winner = pl1
        else:
            winner = pl2
        winner.push(cr1)
        winner.push(cr2)
        round += 1
    else:
        if pl1.size == 0:
            print(f'second {round}')
        else:
            print(f'first {round}')


if __name__ == '__main__':
    run()
