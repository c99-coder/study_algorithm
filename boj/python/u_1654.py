import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())

arr = []
for _ in range(K):
    arr.append(int(input()))
