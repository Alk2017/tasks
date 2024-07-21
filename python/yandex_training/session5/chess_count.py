B = 'B'
R = 'R'
A = 'A'
BUSY = [A, B, R]
FIGURE = [B, R]


def fil_for_b(i, j, board):
    a = i-1
    b = j-1
    while a >= 0 and b >= 0 and board[a][b] not in FIGURE:
        board[a][b] = A
        a -= 1
        b -= 1
    a = i-1
    b = j+1
    while a >= 0 and b < 8 and board[a][b] not in FIGURE:
        board[a][b] = A
        a -= 1
        b += 1
    a = i + 1
    b = j - 1
    while a < 8 and b >= 0 and board[a][b] not in FIGURE:
        board[a][b] = A
        a += 1
        b -= 1
    a = i + 1
    b = j + 1
    while a < 8 and b < 8 and board[a][b] not in FIGURE:
        board[a][b] = A
        a += 1
        b += 1


def fil_for_r(i, j, board):
    a = i - 1
    b = j
    while a >= 0 and board[a][b] not in FIGURE:
        board[a][b] = A
        a -= 1
    a = i + 1
    while a < 8 and board[a][b] not in FIGURE:
        board[a][b] = A
        a += 1
    a = i
    b = j - 1
    while b >= 0 and board[a][b] not in FIGURE:
        board[a][b] = A
        b -= 1
    b = j + 1
    while b < 8 and board[a][b] not in FIGURE:
        board[a][b] = A
        b += 1


def run():
    board = []
    for _ in range(8):
        board.append(list(input()))

    for i in range(8):
        for j in range(8):
            if board[i][j] == B:
                fil_for_b(i, j, board)
            elif board[i][j] == R:
                fil_for_r(i, j, board)

    res = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == '*':
                res += 1
    print(res)


if __name__ == '__main__':
    run()
