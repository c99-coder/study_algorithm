import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for i in range(t):
    arr = input()
    k = int(input())

    alpha = defaultdict(list)

    for i in range(len(arr)):
        if arr.count(arr[i]) >= k:
            alpha[arr[i]].append(i)

    if not alpha:
        print(-1)
    else:
        Min = 10000
        Max = 0

        for x in alpha.values():
            for i in range(len(x)-k+1):
                result = x[i+k-1] - x[i] + 1

                if result < Min:
                    Min = result

                if result > Max:
                    Max = result
        print(Min, Max)
