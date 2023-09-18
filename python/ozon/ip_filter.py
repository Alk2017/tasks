def run():
    c_ip, c_f = [int(i) for i in input().split()]
    ips = []
    for _ in range(c_ip):
        ips.append([int(i) for i in input().split('.')])
    d_ip = dict()
    for ip in ips:
        if ip[2] in d_ip.keys():
            d_ip[ip[2]].append(ip[3])
        else:
            d_ip[ip[2]] = [ip[3]]
    if len(d_ip.keys()) > c_f:
        print(65536 - len(ips))
        print(1)
        print('100.200.0.0/16')
    else:
        add = c_f - len(d_ip.keys())
        m_ls = []
        for k in d_ip.keys():
            m_ls.append((k, len(d_ip[k])))
        m_ls.sort(key=lambda j: j[1])
        res_f = []
        res_m = 0
        for ip, c in m_ls:
            if c == 1:
                res_f.append(f'100.200.{ip}.{d_ip[ip][0]}')
            elif c <= add + 1:
                add -= (c - 1)
                for end in d_ip[ip]:
                    res_f.append(f'100.200.{ip}.{end}')
            else:
                res_f.append(f'100.200.{ip}.0/24')
                res_m += (256 - len(d_ip[ip]))
        print(res_m)
        print(len(res_f))
        for f in res_f:
            print(f)


if __name__ == '__main__':
    run()