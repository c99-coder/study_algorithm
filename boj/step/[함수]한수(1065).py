n = int(input())

count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
        continue
    if i % 10 - i % 100 // 10 == i % 100 // 10 - i // 100:
        count += 1
print(count)
