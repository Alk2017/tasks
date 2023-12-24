def action(o, n1, n2):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    else:
        print('wrong operation')
        return -1


def run():
    line = input().split()
    stack = []
    oper = ['+', '-', '*']
    for op in line:
        if op in oper:
            if len(stack) < 2:
                print('stack hasnot two el')
                break
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(int(action(op, n1, n2)))
        else:
            stack.append(int(op))
    if len(stack) == 1:
        print(stack.pop())
    else:
        print('stack has more one el')


if __name__ == '__main__':
    run()
