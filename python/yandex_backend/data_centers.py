def run():
    dc_c, s_c, cmd_c = [int(i) for i in input().split()]
    # DC1 ([true, true, true], 0, 3)
    # DC1 ([], R, A)
    dcs = [[[True] * s_c, 0, s_c] for _ in range(dc_c)]
    max_v = max_dc = min_v = min_dc = 0
    for _ in range(cmd_c):
        cmd = input().split()
        if cmd[0] == 'DISABLE':
            dc_n = int(cmd[1]) - 1
            dc = dcs[dc_n]
            if dc[0][int(cmd[2]) - 1]:
                dc[2] -= 1
                dc[0][int(cmd[2]) - 1] = False
                new_mtr = dcs[dc_n][1] * dcs[dc_n][2]
                if new_mtr > max_v:
                    max_v = new_mtr
                    max_dc = dc_n
                elif new_mtr < min_v:
                    min_v = new_mtr
                    min_dc = dc_n
        elif cmd[0] == 'RESET':
            dc_n = int(cmd[1]) - 1
            dc = dcs[dc_n]
            dcs[dc_n] = [[True] * s_c, dc[1] + 1, s_c]
            mtr_after_res = dcs[dc_n][1] * dcs[dc_n][2]
            if dc_n == max_dc:
                if mtr_after_res >= max_v:
                    max_v = mtr_after_res
                else:
                    act_max = dcs[0][1] * dcs[0][2]
                    max_s = 0
                    for i in range(1, dc_c):
                        item = dcs[i][1] * dcs[i][2]
                        if item > act_max:
                            act_max = item
                            max_s = i
                    max_dc = max_s
                    max_v = act_max
            elif dc_n == min_dc:
                if mtr_after_res <= min_v:
                    min_v = mtr_after_res
                else:
                    act_min = dcs[0][1] * dcs[0][2]
                    min_s = 0
                    for i in range(1, dc_c):
                        item = dcs[i][1] * dcs[i][2]
                        if item < act_min:
                            act_min = item
                            min_s = i
                    min_dc = min_s
                    min_v = act_min

        elif cmd[0] == 'GETMAX':
            # act_max = dcs[0][1] * dcs[0][2]
            # max_s = 0
            # for i in range(1, dc_c):
            #     item = dcs[i][1] * dcs[i][2]
            #     if item > act_max:
            #         act_max = item
            #         max_s = i
            print(max_dc + 1)
        elif cmd[0] == 'GETMIN':
            # act_min = dcs[0][1] * dcs[0][2]
            # min_s = 0
            # for i in range(1, dc_c):
            #     item = dcs[i][1] * dcs[i][2]
            #     if item < act_min:
            #         act_min = item
            #         min_s = i
            print(min_dc + 1)
        else:
            print('Error: Unknown command.')
            return


if __name__ == '__main__':
    run()

