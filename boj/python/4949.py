import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

for line in sys.stdin.readlines():
    cur_line = line.rstrip()
    if cur_line == '.':
        break
    cur_line = cur_line.replace(" ", "")

    queue = deque()
    flag = 1
    for x in cur_line:
        if x.isalpha() == True or x == '.':
            continue
        if x == '(' or x == '[':
            queue.append(x)
        else:
            if queue:
                if x == ')' and queue.pop() == '(' or x == ']' and queue.pop() == '[':
                    continue
                else:
                    flag = 0
            else:
                flag = 0

    if flag and not queue:
        print("yes")
    else:
        print("no")
