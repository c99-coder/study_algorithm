import sys
import math


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for i in range(n):
    h, w, num = map(int, input().split())
    a = num % h if num % h else h
    b = math.ceil(num/h)
    print('{0}{1:02d}'.format(a, b))
