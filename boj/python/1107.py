import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num = list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    for num in str(nums):
        if int(num) in break_num:
            break
    else:
        min_count = min(min_count, abs(int(nums) - target) + len(str(nums)))

print(min_count)
