class MyQueueSized:

    def __init__(self, max_size):
        self.max_size = max_size
        self.q = [None] * max_size
        self.size = 0
        self.tail = 0
        self.head = 0

    def size_q(self):
        return str(self.size)

    def push(self, item):
        if self.size == self.max_size:
            print('error')
        else:
            self.q[self.tail] = item
            self.tail = self.tail + 1 % self.max_size
            self.size += 1

    def peek(self):
        if self.size == 0:
            return None
        else:
            return str(self.q[self.head])

    def pop(self):
        if self.size == 0:
            return None
        else:
            item = self.q[self.head]
            self.q[self.head] = None
            self.head = self.head + 1 % self.max_size
            self.size -= 1
            return str(item)


if __name__ == '__main__':
    count = int(input())
    size = int(input())
    q = MyQueueSized(size)
    for _ in range(count):
        com = input().split()
        if com[0] == 'push':
            q.push(com[1])
        elif com[0] == 'peek':
            print(q.peek())
        elif com[0] == 'pop':
            print(q.pop())
        elif com[0] == 'size':
            print(q.size_q())
        else:
            print('error')