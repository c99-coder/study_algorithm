import sys


def input():
    return sys.stdin.readline().rstrip()


t = int(input())

fib = [0] * 41
fib[1] = 1
fib[2] = 1
for i in range(3, 41):
    fib[i] = fib[i-1] + fib[i-2]

for i in range(t):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        print(fib[n-1], fib[n])
