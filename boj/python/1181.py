# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())

arr = set()
for _ in range(N):
    arr.add(input())


answer = sorted(list(arr))
answer.sort(key=len)

for i in range(len(answer)):
    print(answer[i])
