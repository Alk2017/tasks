def find_round(step):
    round = 0
    count = 0
    prev_count = 0
    i = 1
    while True:
        if step <= count:
            return round, step - prev_count
        prev_count = count
        count += i * 8
        round += 1
        i += 1


def find_robot(step):
    if step == 0:
        return 0, 0
    cur_round, cur_step = find_round(step)  # 3
    # = step - (8 * (cur_round - 1))  # 2
    c_in_row = cur_round * 8 // 4  # 2
    cur_q = (cur_step - 1) // c_in_row  # 0
    c_in_q = (cur_step - 1) % c_in_row  # 0
    if cur_q == 0:
        start_in_q = -1 * cur_round, cur_round - 1
        return start_in_q[0], start_in_q[1] - c_in_q
    elif cur_q == 1:
        start_in_q = -1 * (cur_round - 1), -1 * cur_round
        return start_in_q[0] + c_in_q, start_in_q[1]
    elif cur_q == 2:
        start_in_q = cur_round, -1 * (cur_round - 1)
        return start_in_q[0], start_in_q[1] + c_in_q
    elif cur_q == 3:
        start_in_q = cur_round - 1, cur_round
        return start_in_q[0] - c_in_q, start_in_q[1]
    else:
        return -1, -1


def run():
    file_in = open('input.txt', 'r')
    file_out = open('output.txt', 'a')
    step = int(file_in.readline())
    answer = ' '.join([str(i) for i in find_robot(step)])
    file_out.write(answer)
    file_in.close()
    file_out.close()


if __name__ == '__main__':
    run()

    # assert find_robot(0) == (0, 0), f'{find_robot(0)}'
    # assert find_robot(1) == (-1, 0), f'{find_robot(1)}'
    # assert find_robot(2) == (-1, -1), f'{find_robot(2)}'
    # assert find_robot(3) == (0, -1), f'{find_robot(3)}'
    # assert find_robot(4) == (1, -1), f'{find_robot(4)}'
    # assert find_robot(5) == (1, 0), f'{find_robot(5)}'
    # assert find_robot(6) == (1, 1), f'{find_robot(6)}'
    # assert find_robot(7) == (0, 1), f'{find_robot(7)}'
    # assert find_robot(8) == (-1, 1), f'{find_robot(8)}'
    # assert find_robot(9) == (-2, 1), f'{find_robot(9)}'
    # assert find_robot(10) == (-2, 0), f'{find_robot(10)}'
    # assert find_robot(11) == (-2, -1), f'{find_robot(11)}'
    # assert find_robot(12) == (-2, -2), f'{find_robot(12)}'
    # assert find_robot(13) == (-1, -2), f'{find_robot(13)}'
    # assert find_robot(14) == (0, -2), f'{find_robot(14)}'
    # assert find_robot(15) == (1, -2), f'{find_robot(15)}'
    # assert find_robot(16) == (2, -2), f'{find_robot(16)}'
    # assert find_robot(17) == (2, -1), f'{find_robot(17)}'
    # assert find_robot(18) == (2, 0), f'{find_robot(18)}'
    # assert find_robot(19) == (2, 1), f'{find_robot(19)}'
    # assert find_robot(20) == (2, 2), f'{find_robot(20)}'
    # assert find_robot(21) == (1, 2), f'{find_robot(21)}'
    # assert find_robot(22) == (0, 2), f'{find_robot(22)}'
    # assert find_robot(23) == (-1, 2), f'{find_robot(23)}'
    # assert find_robot(24) == (-2, 2), f'{find_robot(24)}'
    # assert find_robot(25) == (-3, 2), f'{find_robot(25)}'
    # assert find_robot(27) == (-3, 0), f'{find_robot(27)}'
    # assert find_robot(30) == (-3, -3), f'{find_robot(30)}'
    # assert find_robot(33) == (0, -3), f'{find_robot(33)}'
    # assert find_robot(36) == (3, -3), f'{find_robot(36)}'
    # assert find_robot(39) == (3, 0), f'{find_robot(39)}'
    # assert find_robot(42) == (3, 3), f'{find_robot(42)}'
    # assert find_robot(45) == (0, 3), f'{find_robot(45)}'
    # assert find_robot(48) == (-3, 3), f'{find_robot(48)}'
    # assert find_robot(49) == (-4, 3), f'{find_robot(49)}'
