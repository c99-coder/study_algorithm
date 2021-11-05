import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
m = int(input())
arr = [i for i in range(m+1)]
arr[1] = 0

for i in range(2, m+1):
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = 0

arr2 = []
for i in arr[n:]:
    if i != 0:
        arr2.append(i)

if len(arr2) == 0:
    print(-1)
else:
    print(sum(arr2))
    print(min(arr2))
