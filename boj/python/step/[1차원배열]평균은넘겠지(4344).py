import sys


def input():
    return sys.stdin.readline().rstrip()


_list = []
n = int(input())
for i in range(n):
    _list = list(map(int, input().split()))
    m = _list.pop(0)
    _avg = sum(_list) / m

    count = 0
    for j in _list:
        if j > _avg:
            count += 1

    print('{0:0.3f}%'.format(count / m * 100))
