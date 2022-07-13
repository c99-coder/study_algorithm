import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = 1_000_000_000

while start <= end:
    mid = (start + end) // 2

    trees = 0
    for i in l:
        if i - mid > 0:
            trees += i - mid

    if trees >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
