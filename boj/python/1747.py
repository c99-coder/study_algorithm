n = int(input())


def solution(n):
    max = 1_000_000

    arr = [True for _ in range(max+1)]
    arr[1] = False

    for i in range(2, max+1):
        if arr[i]:
            if i >= n:
                if str(i) == str(i)[::-1]:
                    return i
            for j in range(2*i, max+1, i):
                arr[j] = False

    return 1003001


result = solution(n)
print(result)
