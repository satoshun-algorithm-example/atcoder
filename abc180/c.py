from itertools import combinations
import math


def prime_factors(n):
    if n < 2:
        return []

    factors = []
    for p in range(2, int(n ** 0.5) + 1):
        while n % p == 0:
            factors.append(p)
            n //= p

    if n > 1:
        factors.append(n)

    return factors


N = int(input())

factors = prime_factors(N)

result = {1}

for i in range(1, len(factors) + 1):
    for j in combinations(factors, i):
        result.add(math.prod(j))

result = sorted(list(result))

for r in result:
    print(r)
