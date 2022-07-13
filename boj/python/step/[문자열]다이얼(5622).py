n = input()
arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', "TUV", "WXYZ"]

sum = 0
for i in n:
    for index, j in enumerate(arr):
        if i in j:
            sum += index+3
print(sum)
