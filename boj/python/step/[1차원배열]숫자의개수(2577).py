import sys


def input():
    return sys.stdin.readline().rstrip()


a = int(input())
b = int(input())
c = int(input())
_mul = str(a*b*c)

for i in range(10):
    print(_mul.count(str(i)))
