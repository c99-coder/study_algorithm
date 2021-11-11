from copy import deepcopy
import sys


def input():
    return sys.stdin.readline().rstrip()


def Solution():
    r, c, m = map(int, input().split())

    board = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(m):
        row, col, speed, direction, size = map(int, input().split())
        board[row-1][col-1] = [speed, direction-1, size]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, 1, -1)

    result = 0
    for j in range(c):
        for i in range(r):
            if board[i][j] != 0:
                result += board[i][j][2]
                board[i][j] = 0
                break

        temp_board = [[0 for _ in range(c)] for _ in range(r)]
        for j in range(c):
            for i in range(r):
                if board[i][j] != 0:  # [speed, direction-1, size]
                    speed = board[i][j][0]
                    dir = board[i][j][1]

                    if dir == 0 or dir == 1:
                        speed = speed % ((r-1)*2)
                    elif dir == 2 or dir == 3:
                        speed = speed % ((c-1)*2)

                    x, y = i, j
                    tx, ty = dx[dir], dy[dir]

                    while True:
                        if -1 < x+tx*speed < r and -1 < y+ty*speed < c:
                            nx = x+tx*speed
                            ny = y+ty*speed
                            break

                        if dir == 0:
                            speed -= x
                            tx, ty = dx[1], dy[1]
                            x = 0
                            dir = 1

                        elif dir == 1:
                            speed -= r-x-1
                            tx, ty = dx[0], dy[0]
                            x = r-1
                            dir = 0

                        elif dir == 2:
                            speed -= c-y-1
                            tx, ty = dx[3], dy[3]
                            y = c-1
                            dir = 3

                        elif dir == 3:
                            speed -= y
                            tx, ty = dx[2], dy[2]
                            y = 0
                            dir = 2

                    if temp_board[nx][ny] == 0:
                        temp_board[nx][ny] = [board[i][j]
                                              [0], dir, board[i][j][2]]
                    else:
                        if temp_board[nx][ny][2] < board[i][j][2]:
                            temp_board[nx][ny] = [board[i][j]
                                                  [0], dir, board[i][j][2]]
        board = deepcopy(temp_board)

    return result


print(Solution())
