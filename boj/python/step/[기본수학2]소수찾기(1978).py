import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
_list = list(map(int, input().split()))
_max = max(_list)
arr = [0, 0] + [1]*(_max-1)

for i in range(2, _max+1):
    if arr[i]:
        for j in range(2*i, _max+1, i):
            arr[j] = 0

count = 0
for i in _list:
    if arr[i] != 0:
        count += 1

print(count)
