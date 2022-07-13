import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def BFS(ground, root):
    visited = set()
    queue = deque([root])
    dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            for dx, dy in dir:
                nx, ny = cx + dx, cy + dy
                if -1 < nx < M and -1 < ny < N and ground[ny][nx] == 1:
                    queue.append([nx, ny])
    return visited


T = int(input())
for testcase in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    visited = set()
    ans = [0] * T
    for i in range(M):
        for j in range(N):
            if (i, j) not in visited and ground[j][i] == 1:
                visited |= BFS(ground, (i, j))
                ans[testcase] += 1
    print(ans[testcase])
