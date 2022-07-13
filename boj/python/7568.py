import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')

N = int(input())

l = []
for _ in range(N):
    l.append(list(map(int, input().split()))+[1])

for i in range(N-1):
    x1, y1, score1 = l[i]
    for j in range(1, N-i):
        x2, y2, score2 = l[i+j]
        if x1 > x2 and y1 > y2:
            l[i+j][2] += 1
        elif x1 < x2 and y1 < y2:
            l[i][2] += 1

for _, _, score in l:
    print(score, end=' ')
