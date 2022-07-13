import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, K = map(int, input().split())

_time = 0
queue = deque(N)
visited = set()
flag = True

cur_nums = []
while flag:
    while queue:
        cur_nums.append(queue.popleft())

    for num in cur_nums:
        if num == K:
            flag = False
        if 0 <= num <= 100000 and num not in visited:
            visited.add(num)
            queue.extend([num+1, num-1, num*2])
    _time += 1

print(_time)
