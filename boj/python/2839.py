import sys


def input():
    return sys.stdin.readline()


sys.stdin = open('input.txt', 'r')


N = int(input())

tmp = N // 5
answer = 5001

for i in range(tmp, -1, -1):
    tmp = 5 * i
    if N - tmp == 0:
        answer = min(answer, i)
        break
    elif (N - tmp) % 3 == 0:
        answer = min(answer, i + (N - tmp) // 3)

if answer == 5001:
    print(-1)
else:
    print(answer)
