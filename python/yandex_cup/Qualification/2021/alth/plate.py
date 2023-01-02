def print_plate(p):
    print(p[:2], p[:-3:-1], sep='\n', end='\n\n')


if __name__ == '__main__':
    # count = int(input())
    count = 1
    plates = ['WWWB']
    # for _ in range(0, count*2):
    #     plates.append(input())
    print_plate(plates[0])

    # x, y = map(lambda _: int(_), input().split())
    x, y = 2, 4
    picture = ['WBWW']
    # for _ in range(0, x):
    #     picture.append(input())
    print('end')
