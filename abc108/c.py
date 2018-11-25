n, k = map(int, input().split())

zero = n // k
c = 1
for i in range(zero-1):
    c *= 8

if k % 2 == 0:
    half = k // 2
    d = 0
    for i in range(1, n+1):
        if i % k == half:
            d += 1
    a = 1
    for i in range(d-1):
        a *= 8
    c += a

print(c)
