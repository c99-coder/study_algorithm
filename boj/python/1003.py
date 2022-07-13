import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

fib = [[] for _ in range(41)]
fib[0] = [1, 0]
fib[1] = [0, 1]

for i in range(2, 41):
    fib[i] = [fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1]]

T = int(input())
for _ in range(T):
    N = int(input())
    print(*fib[N])
