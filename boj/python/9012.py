import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

N = int(input())

for i in range(N):
    string = input().rstrip()
    queue = []
    flag = 1
    for x in string:
        if x == '(':
            queue.append('(')
        else:
            if queue:
                queue.pop()
            else:
                flag = 0

    if not queue and flag:
        print("YES")
    else:
        print("NO")
