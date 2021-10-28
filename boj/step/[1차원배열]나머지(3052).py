import sys


def input():
    return sys.stdin.readline().rstrip()


visited = set()

count = 10
for i in range(10):
    n = int(input())
    if n % 42 in visited:
        count -= 1
    else:
        visited.add(n % 42)

print(count)
