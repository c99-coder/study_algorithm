import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
stairs = []

for _ in range(n):
    stairs.append(int(input()))

if len(stairs) == 1:
    print(stairs[0])

elif len(stairs) == 2:
    print(stairs[0]+stairs[1])

else:
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
    print(dp[n-1])
