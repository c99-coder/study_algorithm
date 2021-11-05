import sys


def input():
    return sys.stdin.readline().rstrip()


dp = [[i for i in range(1, 15)] for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 14):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

# print(dp)
num = int(input())
for _ in range(num):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])
