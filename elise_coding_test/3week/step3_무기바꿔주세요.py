n = int(input())

dp = [0] * 21
dp[2] = 1

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) * (i-1)

print(dp[n])
