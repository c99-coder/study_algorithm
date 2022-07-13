import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
a = map(int, input().split())
b = map(int, input().split())

dict_a = dict()
dict_b = dict()

for i in a:
    if i not in dict_a:
        dict_a[i] = 1
    else:
        dict_a[i] = dict_a[i] + 1

for i in b:
    if i not in dict_b:
        dict_b[i] = 1
    else:
        dict_b[i] = dict_b[i] + 1

result = 0
for i in dict_a:
    if i in dict_b:
        result += dict_a[i] - dict_b[i] if dict_a[i] - dict_b[i] > 0 else 0
    else:
        result += dict_a[i]

print(result)
