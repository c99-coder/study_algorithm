from collections import deque
from functools import reduce
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

# 2차원 리스트의 정보 입력받기
puzzle = [list(map(int, input().split())) for _ in range(n)]


# 리스트에 있는 값 모두 곱하기
def multiply(arr):
    return reduce(lambda x, y: x * y, arr)


def bfs(x, y):
    # 하, 우
    dx, dy = (1, 0), (0, 1)

    queue = deque()
    queue.append((x, y))

    maxNum = 0
    mulTempList = [0] * 4
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # 현제 위치에서 하, 우 방향으로의 위치 확인
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or puzzle[nx][ny] == 0:
                continue
            queue.append((nx, ny))

        # 하, 우, 좌하->우상 대각, 좌상->우하 대각 곱셈
        if x + 3 < n:
            mulTempList[0] = (
                multiply([puzzle[x + index][y]for index in range(4)]))
        if y + 3 < n:
            mulTempList[1] = (
                multiply([puzzle[x][y + index] for index in range(4)]))
        if x - 3 >= 0 and y + 3 < n:
            mulTempList[2] = (
                multiply([puzzle[x - index][y + index] for index in range(4)]))
        if x + 3 < n and y + 3 < n:
            mulTempList[3] = (
                multiply([puzzle[x + index][y + index] for index in range(4)]))

        print("value={:<2}".format(
            puzzle[x][y]), '['+str(x)+']'+'['+str(y)+']', *mulTempList)

        # 최대값 구하기
        maxNum = max(maxNum, *mulTempList)

        # 0으로 초기화하기
        mulTempList = [0 for _ in range(4)]

    return maxNum


print(bfs(0, 0))
