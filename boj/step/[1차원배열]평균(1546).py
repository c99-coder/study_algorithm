import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
_list = list(map(int, input().split()))
m = max(_list)

for index, i in enumerate(_list):
    _list[index] = i / m * 100

print(sum(_list)/len(_list))
