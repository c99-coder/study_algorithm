from sys import stdin
input = stdin.readline

# 함정 개수 변수
count = 0

# 1줄씩 행을 받아옴, 행의 index 변수 i
for i, line in enumerate([input().strip() for _ in range(8)]):
    # 1개씩 값을 받아옴, 열의 index 변수 j
    for j, element in enumerate(line):
        if element == 'H':
            # 홀수 행은 홀수 열 위치에, 짝수 행은 짝수 열 위치에 함정이 있음
            if i % 2 == 1 and j % 2 == 1:
                count += 1
            elif i % 2 == 0 and j % 2 == 0:
                count += 1

print(count)
