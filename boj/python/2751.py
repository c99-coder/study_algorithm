import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt', 'r')


N = int(input())

l = []
for i in range(N):
    l.append(int(input()))
l.sort()

print('\n'.join(map(str, l)))
