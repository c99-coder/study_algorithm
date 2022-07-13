n = input()
arr = [0] * 26

for i in n:
    if i.islower:
        i = i.upper()
    arr[ord(i)-65] += 1
_max = max(arr)
if arr.count(_max) > 1:
    print('?')
else:
    print(chr(arr.index(_max)+65))
