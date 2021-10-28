import sys


def input():
    return sys.stdin.readline().rstrip()


_list = []
for i in range(9):
    _list.append(int(input()))
_max = max(_list)
print(_max)
print(_list.index(_max)+1)
