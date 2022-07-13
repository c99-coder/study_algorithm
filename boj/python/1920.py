import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

n = input()
N = set(input().split())
m = input()
M = input().split()

for l in M:
    if l in N:
        print(1)
    else:
        print(0)
