a, b, c = map(int, input().split())

if 1 > c - b:
    print(-1)
else:
    print(a // (c - b) + 1)
