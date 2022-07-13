import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
m = int(input())

visited = set()

graph = [[] for _ in range(n+1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

queue = deque([1])
count = 0
while queue:
    node = queue.popleft()

    if node not in visited:
        visited.add(node)
        count += 1

        for v in graph[node]:
            if v not in visited:
                queue.append(v)

print(count-1)
