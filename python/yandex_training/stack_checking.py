class MyStack:
    def __init__(self):
        self.stack = []
        # self.size = 0

    def push(self, item):
        self.stack.append(item)
        # self.size += 1
        print('ok')

    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            last = self.stack.pop()
            # self.size -= 1
            print(last)

    def back(self):
        if len(self.stack) == 0:
            print('error')
        else:
            print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print('ok')


def run():
    cmd = input().split()
    stack = MyStack()
    while cmd[0] != 'exit':
        if cmd[0] == 'push':
            stack.push(cmd[1])
        elif cmd[0] == 'pop':
            stack.pop()
        elif cmd[0] == 'back':
            stack.back()
        elif cmd[0] == 'size':
            stack.size()
        elif cmd[0] == 'clear':
            stack.clear()
        else:
            print('unknown command')
            break
        cmd = input().split()
    else:
        print('bye')


if __name__ == '__main__':
    run()
