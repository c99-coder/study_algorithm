import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
_sum = []
for tmp in input().split('-'):
    _sum.append(sum(list(map(int, tmp.split('+')))))

n = _sum[0]
for i in _sum[1:]:
    n -= i

print(n)
