def run():
    count = int(input())
    if count > 0:
        prev = int(input())
        print(prev)
        for _ in range(count-1):
            act = int(input())
            if act != prev:
                print(act)
                prev = act


if __name__ == '__main__':
    run()