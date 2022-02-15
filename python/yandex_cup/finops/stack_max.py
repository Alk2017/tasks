class StackMax:
    def __init__(self):
        self.items = []
        self.m = []

    def push(self, i):
        self.items.append(i)
        if len(self.m) == 0 or i >= self.m[-1]:
            self.m.append(i)

    def pop(self):
        item = self.items.pop()
        if len(self.m) != 0 and item == self.m[-1]:
            self.m.pop()

    def max_item(self):
        if len(self.items) == 0:
            return None
        return self.m[-1]


def run():
    file_in = open('input.txt', 'r')
    count = int(file_in.readline())
    stack = StackMax()
    for _ in range(count):
        com = file_in.readline().split()
        if com[0] == 'push':
            stack.push(int(com[1]))
        elif com[0] == 'pop':
            stack.pop()
        elif com[0] == 'max':
            print(stack.max_item())
        else:
            print('unknown command')
    file_in.close()


if __name__ == '__main__':
    run()