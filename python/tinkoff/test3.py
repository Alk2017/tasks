if __name__ == '__main__':
    count, t = map(lambda i: int(i), input().split())
    floors = list(map(lambda i: int(i), input().split()))
    l = int(input())
    time = 0
    for i, v in enumerate(floors):
        if t == 0 or count == 0 or l == 0:
            break
        elif i + 1 == len(floors):
            break
        elif i == l-1 and time > t:
            time = -1
            break
        else:
            time += floors[i + 1] - v
    if time == -1:
        if floors[l-1] - floors[0] <= floors[-1] - floors[l-1]:
            time = floors[l-1] - floors[0]
            floors.remove(floors[l - 1])
            for i, v in enumerate(floors):
                if i + 1 == len(floors):
                    break
                else:
                    time += floors[i + 1] - v
        else:
            time = floors[-1] - floors[l-1]
            floors.remove(floors[l - 1])
            floors.reverse()
            for i, v in enumerate(floors):
                if i + 1 == len(floors):
                    break
                else:
                    time += v - floors[i + 1]
    print(time)
