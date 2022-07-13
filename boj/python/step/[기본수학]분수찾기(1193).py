x = int(input())

m = 1
while x > m:
    x -= m
    m += 1

if m % 2 == 0:
    a = x
    b = m-x+1
else:
    a = m-x+1
    b = x

print(a, '/', b, sep='')
