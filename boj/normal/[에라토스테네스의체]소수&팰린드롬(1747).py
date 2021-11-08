n = map(int, input().split())

arr = [True for _ in range(n+1)]
arr[1] = False

for i in range(2, n+1):
    if arr[i]:
        for j in range(2*i, n+1, i):
            arr[j] = 0
        if str(i) == ''.join(list(str(i))[::-1]):
            print(i)
