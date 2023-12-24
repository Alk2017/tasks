def run():
    seq = input()
    stack = []
    for br in seq:
        if br == '(' or br == '[' or br == '{':
            stack.append(br)
        elif br == ')' or br == ']' or br == '}':
            if len(stack) == 0:
                print('no')
                break
            last = stack.pop()
            if 2 >= ord(br) - ord(last) >= 1:
                continue
            else:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    run()
