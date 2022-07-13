import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
count = n

for i in range(n):
    m = list(input())
    temp = ''
    while len(m) > 1:
        temp = m.pop(0)
        if temp != m[0] and temp in m:
            count -= 1
            break

print(count)
