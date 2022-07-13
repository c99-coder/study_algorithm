n, m = map(int, input().split())

arr = [True for _ in range(m+1)]
arr[1] = False

for i in range(2, m+1):
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = 0
        if n <= i:
            print(i)
