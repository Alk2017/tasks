if __name__ == '__main__':
    ls = [1, 2, 3]

    for a in ls:
        print(f'for a = {a}')
        if a == 2:
            print('continue')
            continue
        if a == 4:
            print('break')
            break
    else:
        # only without break
        print('else')
    print('end')

