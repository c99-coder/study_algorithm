import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# DFS
visited = set()
queue = list([v])
while queue:
    node = queue.pop()
    if node not in visited:
        visited.add(node)
        temp = sorted(graph[node], reverse=True)
        print(node, end=' ')
        queue += temp

print()

# BFS
visited = set()
queue = deque([v])
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        temp = sorted(graph[node])
        print(node, end=' ')
        queue += temp
