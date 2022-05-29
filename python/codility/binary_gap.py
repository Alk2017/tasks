def run(n=None):
    if n is None:
        n = int(input())
    # print(n)
    n_s = ''
    for i in range(31, -1, -1):
        if n // (2 ** i) == 1:
            n_s += '1'
            n %= (2 ** i)
        elif len(n_s) != 0:
            n_s += '0'
    # print(n_s)
    gap = m_gap = 0
    for ch in n_s:
        if ch == '1':
            m_gap = max(m_gap, gap)
            gap = 0
        else:
            gap += 1
    # print(m_gap)
    return m_gap


if __name__ == '__main__':
    run(1500)
