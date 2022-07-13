import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

K = int(input())

queue = []
for n in sys.stdin.readlines():
    n = int(n.rstrip())
    if n != 0:
        queue.append(n)
    else:
        queue.pop()

print(sum(queue))
