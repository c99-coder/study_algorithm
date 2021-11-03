num = int(input())

Max = 1
while num != 1:
    Max = max(Max, num)
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
print(Max)
