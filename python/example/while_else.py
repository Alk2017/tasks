if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5]

    i = 0
    while i < len(ls):
        print(f'while a = {ls[i]}')
        if ls[i] == 2:
            print('continue')
            i += 1
            continue
        if ls[i] == 4:
            print('break')
            i += 1
            break
        i += 1
    else:
        # only without break, even for []
        print('else')
    print('end')

