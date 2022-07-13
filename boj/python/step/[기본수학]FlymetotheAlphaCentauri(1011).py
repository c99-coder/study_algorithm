import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    move = 1
    move_plus = 0
    while move_plus < distance:
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0:  # count가 2의 배수일 때,
            move += 1
    print(count)
