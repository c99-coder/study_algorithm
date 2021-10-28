import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
_list = [input() for _ in range(n)]

for i in _list:
    count = 0
    accum = 1
    for j in i:
        if j is 'O':
            count += accum
            accum += 1
        else:
            accum = 1
    print(count)
