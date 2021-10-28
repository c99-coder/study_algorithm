n1 = int(input())
n2 = n1 * 2

arr = [0, 0] + [1]*(n2-1)

for i in range(2, n2+1):
    if arr[i]:
        for j in range(2*i, n2+1, i):
            arr[j] = 0

print(sum(arr[n1:n2+1]))
