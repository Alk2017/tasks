class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __del__(self):
        self.prev = None
        self.next = None
        self.value = None


class MyDeque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def push_front(self, v):
        node = Node(v)
        if self.size == 0:
            self.front = self.back = node
        elif self.size == 1:
            self.front = node
            node.next = self.back
            self.back.prev = node
        else:
            self.front.prev = node
            node.next = self.front
            self.front = node
        self.size += 1
        print('ok')

    def push_back(self, v):
        node = Node(v)
        if self.size == 0:
            self.front = self.back = node
        elif self.size == 1:
            self.back = node
            node.prev = self.front
            self.front.next = node
        else:
            self.back.next = node
            node.prev = self.back
            self.back = node
        self.size += 1
        print('ok')

    def pop_front(self):
        if self.size == 0:
            print('error')
            return None
        elif self.size == 1:
            old_v = self.front.value
            del self.front
            self.front = self.back = None
            self.size = 0
            print(old_v)
        else:
            old = self.front
            v = old.value
            self.front = self.front.next
            del old
            self.front.prev = None
            self.size -= 1
            print(v)

    def pop_back(self):
        if self.size == 0:
            print('error')
            return None
        elif self.size == 1:
            old_v = self.back.value
            del self.back
            self.front = self.back = None
            self.size = 0
            print(old_v)
        else:
            old = self.back
            v = old.value
            self.back = self.back.prev
            del old
            self.back.next = None
            self.size -= 1
            print(v)

    def get_front(self):
        if self.size == 0:
            print('error')
            return None
        else:
            print(self.front.value)

    def get_back(self):
        if self.size == 0:
            print('error')
            return None
        else:
            print(self.back.value)

    def __len__(self):
        return self.size

    def clear(self):
        first = self.front
        while first is not self.back:
            first = self.front.next
            del self.front
        del first
        self.front = None
        self.back = None
        self.size = 0
        print('ok')


def run():
    cmd = input().split()
    deque = MyDeque()
    while cmd[0] != 'exit':
        if cmd[0] == 'push_front':
            deque.push_front(cmd[1])
        elif cmd[0] == 'push_back':
            deque.push_back(cmd[1])
        elif cmd[0] == 'pop_front':
            deque.pop_front()
        elif cmd[0] == 'pop_back':
            deque.pop_back()
        elif cmd[0] == 'front':
            deque.get_front()
        elif cmd[0] == 'back':
            deque.get_back()
        elif cmd[0] == 'size':
            print(len(deque))
        elif cmd[0] == 'clear':
            deque.clear()
        else:
            print('unknown command')
            break
        cmd = input().split()
    else:
        print('bye')


if __name__ == '__main__':
    run()

