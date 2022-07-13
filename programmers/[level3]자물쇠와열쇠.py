import copy


def check(i, j, n, m, key, temp_board):
    for x in range(n):
        for y in range(n):
            temp_board[i+x][j+y] += key[x][y]

    for i in range(m):
        for j in range(m):
            if temp_board[i+n][j+n] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)

    board = [[0] * (m*2+n) for _ in range(m*2+n)]

    for i in range(m):
        for j in range(m):
            board[i+n][j+n] = lock[i][j]

    # for i in board:
    #     print(i)

    temp_board = copy.deepcopy(board)
    for _ in range(4):

        key = [k[::-1] for k in zip(*key)]
        # for x in key:
        #     print(x)
        for i in range(1, n+m):
            for j in range(1, n+m):
                if True == check(i, j, n, m, key, temp_board):
                    return True
                # for x in temp_board:
                #     print(x)
                temp_board = copy.deepcopy(board)
                # print()
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
