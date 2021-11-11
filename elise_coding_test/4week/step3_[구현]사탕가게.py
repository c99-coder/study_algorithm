num = int(input())

Max = 1
while num != 1:
    Max = max(Max, num)
    # 짝수라면 2로 나눈다.
    if num % 2 == 0:
        num = num // 2
    # 홀수라면 3을 곱한 뒤 1을 더한다.
    else:
        num = num * 3 + 1
print(Max)
