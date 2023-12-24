def get_half(d):
    if d < 0:
        d += 24*3600
    if d % 2 == 0:
        return d // 2
    else:
        return (d // 2) + 1


def date_format(s):
    res = ['']*3
    s %= 3600*24
    h = s // 3600
    s -= h * 3600
    m = s // 60
    s -= m * 60
    if h < 10:
        res[0] += f'0{h}'
    else:
        res[0] += f'{h}'
    if m < 10:
        res[1] += f'0{m}'
    else:
        res[1] += f'{m}'
    if s < 10:
        res[2] += f'0{s}'
    else:
        res[2] += f'{s}'
    return ':'.join(res)



# 3665 -> 3600 60 5 -> 01:01:05
# 5789 -> 3600 2189 -> 3600 2160 29 -> 01:36:29

def run():
    sent = [int(i) for i in input().split(':')]
    sent_s = sent[0] * 3600 + sent[1] * 60 + sent[2]
    exactly = [int(i) for i in input().split(':')]
    exactly_s = exactly[0] * 3600 + exactly[1] * 60 + exactly[2]
    receive = [int(i) for i in input().split(':')]
    receive_s = receive[0] * 3600 + receive[1] * 60 + receive[2]
    delta = get_half(receive_s - sent_s)
    print(date_format(exactly_s+delta))


if __name__ == '__main__':
    run()
    # print(get_half(3))
    # print(date_format(578999))
