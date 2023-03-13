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


def run():
    buf = MyRingBuff(3)
    print('h')


if __name__ == '__main__':
    run()
