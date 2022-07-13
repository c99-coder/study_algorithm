import sys
from collections import deque


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(enumerate(map(int, input().split())))
    cnt = 0

    while queue:
        max_level = max([i[1] for i in queue])
        tmp = queue.popleft()

        if max_level > tmp[1]:
            queue.append(tmp)

        else:
            cnt += 1
            if tmp[0] == M:
                break

    print(cnt)
