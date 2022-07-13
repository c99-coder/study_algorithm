n = input()

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

index = 0
count = 0
count2 = 0

while index != len(n):
    for x in arr:
        if n[index:index+len(x)] == x:
            index += len(x)
            count += 1
            count2 = 0
            break
        else:
            count2 += 1
    if count2 > 7:
        count += 1
        index += 1
print(count)
