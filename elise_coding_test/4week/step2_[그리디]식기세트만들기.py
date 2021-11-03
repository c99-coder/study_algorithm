c, s, e = map(int, input().split())

for i in range(e):
    if c//2 < s:
        s -= 1
    else:
        c -= 1

print(min(c//2, s))
