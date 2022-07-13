import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())

deque = deque([i for i in range(1, N+1)])

answer = []
while deque:
    for _ in range(K):
        deque.append(deque.popleft())
    answer.append(deque.pop())
print(f"<{str(answer)[1:-1]}>")
