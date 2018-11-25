from itertools import product
n, k = map(int, input().split())

zero = n // k
c = len(list(product(range(zero), repeat=3)))

if k % 2 == 0:
    half = k // 2
    d = 0
    for i in range(1, n+1):
        if i % k == half:
            d += 1
    c += len(list(product(range(d), repeat=3)))

print(c)
