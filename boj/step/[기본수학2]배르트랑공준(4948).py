import sys


def input():
    return sys.stdin.readline().rstrip()


max = 123_456 * 2
arr = [1 for _ in range(max+1)]
arr[0], arr[1] = 0, 0

temp = 0
for i in range(2, max+1):
    if arr[i]:
        for j in range(2*i, max+1, i):
            arr[j] = 0
        temp += 1
        arr[i] = temp
    else:
        arr[i] = temp

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(arr[n*2] - arr[n])
