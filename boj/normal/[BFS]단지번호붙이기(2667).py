from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
Map = [[int(i) for i in input()] for _ in range(n)]


def bfs(x, y):
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    queue = deque()
    queue.append((x, y))

    count = 1

    while queue:
        x, y = queue.popleft()
        Map[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if Map[nx][ny] == 1:
                Map[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


result = []
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
