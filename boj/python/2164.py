import sys
from collections import deque


def input():
    return sys.stdin.readline()


# sys.stdin = open('input.txt', 'r')


N = int(input())
queue = deque([i for i in range(1, N+1)])

while queue:
    tmp = queue.popleft()
    if queue:
        queue.append(queue.popleft())

print(tmp)
