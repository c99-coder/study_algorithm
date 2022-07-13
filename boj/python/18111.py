import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, B = map(int, input().split())

blocks = {}
for _ in range(N):
    for i in list(map(int, input().split())):
        if i in blocks:
            blocks[i] += 1
        else:
            blocks[i] = 1

sorted_dict = sorted(blocks.items())
_sum = sum(map(lambda x: x[0] * x[1], sorted_dict))
_len = N * M
_min = sorted_dict[0][0]
_max = sorted_dict[-1][0]

minTime = int(10e7)
maxHeight = 0

for height in range(_min, _max + 1):
    if _len * height <= _sum + B:
        time = 0
        for key in blocks:
            if key < height:
                time += (height - key) * blocks[key]
            elif key > height:
                time += (key - height) * blocks[key] * 2
        if time <= minTime:
            minTime = time
            maxHeight = height

print(minTime, maxHeight)
