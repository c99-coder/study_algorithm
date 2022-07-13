import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
_list = list(map(int, input().split()))
print(min(_list), max(_list))
