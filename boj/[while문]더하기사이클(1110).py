n = int(input())

temp = n
count = 0

if temp < 10:
    temp * 10

while True:
    temp = (temp % 10) * 10 + (temp // 10 + temp % 10) % 10

    count += 1
    if n == temp:
        break

print(count)
