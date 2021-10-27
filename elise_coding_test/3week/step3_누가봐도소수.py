n = input()

if '3' in n or '4' in n or '7' in n:
    print('no')

else:
    flipN = []
    for i in n[::-1]:
        if i == '6':
            i = '9'
        elif i == '9':
            i = '6'
        flipN.append(i)
    flipN = ''.join(flipN)

    n = int(n)
    flipN = int(flipN)

    maxN = max(n, flipN)

    arr = [False, False] + [True]*(maxN-1)

    for i in range(2, maxN+1):
        if arr[i]:
            for j in range(2*i, maxN+1, i):
                arr[j] = False

    if arr[n] and arr[flipN]:
        print('yes')
    else:
        print('no')
