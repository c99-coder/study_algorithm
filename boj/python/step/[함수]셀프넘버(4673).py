items = [i for i in range(10001)]

for i in range(1, 10001):
    if items[i]:
        print(items[i])
        check = i
        while True:
            for j in str(check):
                check += int(j)
            if check < 10001:
                if items[check] == 0:
                    continue
                else:
                    items[check] = 0
            else:
                break
