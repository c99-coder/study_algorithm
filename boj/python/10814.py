import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

l = []
N = int(input())
for _ in range(N):
    l.append(input().split())
l.sort(key=lambda x: int(x[0]))

for x, y in l:
    print(x, y)
