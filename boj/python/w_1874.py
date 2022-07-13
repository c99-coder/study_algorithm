import sys
sys.stdin = open('input.txt', 'r')

# N = int(input())

# arr = []
# for _ in range(N):
#     arr.append(int(input()))

# tmp = [i for i in range(1, N+1)]

# queue = []
# answer = []
# while tmp or queue:
#     if not tmp and queue[-1] != arr[0]:
#         answer = "NO"
#         break

#     queue.append(tmp.pop(0))
#     answer.append('+')

#     if queue[-1] == arr[0]:
#         queue.pop()
#         arr.pop(0)
#         answer.append('-')

#     else:
#         queue.append(tmp.pop(0))
#         answer.append('+')

# print('\n'.join(answer))

N = int(input())
stack = []
answer = []
cur = 1
flag = 1
for i in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        flag = 0
        print("NO")
        break

if flag:
    print("\n".join(answer))
