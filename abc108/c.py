n, k = map(int, input().split())

zero = n // k
c = zero * zero * zero

if k % 2 == 0:
    half = k // 2
    d = 0
    for i in range(1, n+1):
        if i % k == half:
            d += 1
    c += (d * d * d)

print(c)
