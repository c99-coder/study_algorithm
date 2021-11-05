import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
arr = [0, 0] + [1]*(m-1)

for i in range(2, m+1):
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = 0
