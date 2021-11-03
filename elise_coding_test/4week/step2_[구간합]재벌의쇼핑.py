import sys


def input():
    return sys.stdin.readline().rstrip()


n, s = map(int, input().split())
goods = list(map(int, input().split()))

if sum(goods) < s:
    print(0)
else:
    min_count = 100001
    for i in range(n):
        sum_temp = 0
        for j in range(i, n):
            sum_temp += goods[j]
            if sum_temp >= s:
                min_count = min(min_count, j-i+1)
                break
    print(min_count)
