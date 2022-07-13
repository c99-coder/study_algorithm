import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

X = int(input())
l = [0] * (X + 1)

for i in range(2, X+1):
    l[i] = l[i-1] + 1
    if i % 3 == 0:
        l[i] = min(l[i], l[i//3] + 1)
    if i % 2 == 0:
        l[i] = min(l[i], l[i//2] + 1)
print(l[X])
