import sys


def main():
    n = int(input())
    if n == 0:
        print(-1)
        return
    m = [[-1] * (n + 1)]
    for _ in range(n):
        m.append([-1] + [int(i) for i in input().split()])
    s, f = [int(i) for i in input().split()]
    vis = [False] * (n + 1)
    dist = [sys.maxsize] * (n + 1)
    prev = [-1] * (n + 1)
    dist[s] = 0
    for _ in range(n):
        act_i = -1
        for i in range(1, n + 1):
            if dist[i] != sys.maxsize and not vis[i]:
                act_i = i
                break
        if act_i == -1:
            continue
        act_dist = dist[act_i] + 1
        for j in range(1, n + 1):
            if m[act_i][j] == 1:
                if act_dist < dist[j]:
                    dist[j] = act_dist
                    prev[j] = act_i
        vis[act_i] = True
    if dist[f] == sys.maxsize:
        print(-1)
    elif dist[f] == 0:
        print(0)
    else:
        print(dist[f])
        res = [f]
        prev_i = prev[f]
        while prev_i != s:
            res.append(prev_i)
            prev_i = prev[prev_i]
        else:
            res.append(s)
        res.reverse()
        print(' '.join([str(i) for i in res]))


if __name__ == '__main__':
    main()