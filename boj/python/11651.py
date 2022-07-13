import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())

xy = []
for _ in range(N):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x: (x[1], x[0]))

for x, y in xy:
    print(x, y)
