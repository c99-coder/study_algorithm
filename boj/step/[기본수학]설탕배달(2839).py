n = int(input())

temp5 = n//5
result = 5001

for i in range(temp5, -1, -1):
    temp5 = 5 * i
    temp_n = n - temp5
    if temp_n == 0:
        result = min(result, i)
        break
    elif temp_n % 3 == 0:
        result = min(result, i + (temp_n // 3))

if result == 5001:
    print(-1)
else:
    print(result)
