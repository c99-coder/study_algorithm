# import sys
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

arr = []
for _ in range(N):
    arr.append(input())

for i in range(N):
    for j in range(M):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            tmp = 'W'
        else:
            tmp = 'B'
        if arr[i][j] != tmp:
            board[i][j] = 1

# for i in range(N):
#     print(board[i])

min = 64
for i in range(N-7):
    for j in range(M-7):
        tmp = 0
        for k in range(8):
            tmp += sum(board[i+k][j:j+8])

        if tmp > 32:
            tmp = 64 - tmp

        if min > tmp:
            min = tmp

print(min)
