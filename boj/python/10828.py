import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

N = int(input())

queue = []
for i in range(N):
    l = input().rstrip()
    if l[:4] == 'push':
        queue.append(l.split()[1])
    elif l == 'pop':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif l == 'size':
        print(len(queue))
    elif l == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif l == 'top':
        if queue:
            print(queue[-1])
        else:
            print(-1)
