import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dict = {}
N, M = map(int, input().split())
for id in range(1, N+1):
    name = input().strip()
    dict[name] = id
    dict[id] = name

for _ in range(M):
    tmp = input().strip()
    if tmp.isdigit():
        print(dict[int(tmp)])
    else:
        print(dict[tmp])
