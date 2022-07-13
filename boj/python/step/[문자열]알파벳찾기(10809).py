n = input()

arr = [-1] * 26

for index, i in enumerate(n):
    if arr[ord(i)-97] == -1:
        arr[ord(i)-97] = index

print(' '.join(map(str, arr)))
