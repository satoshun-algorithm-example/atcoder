def triangular_relationship(n, k):
    # 1.1: (a + b) % k == 0

    # 1 : a % k + b % k == k
    # 2 : a % k + c % k == k
    # 3 : b % k + c % k == k
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1) :
            for c in range(1, n + 1):
                if a % k + b % k not in (k, 0):
                    continue
                if a % k + c % k not in (k, 0):
                    continue
                if b % k + c % k not in (k, 0):
                    continue
                count += 1
    return count

n, k = map(int, input().split())
print(triangular_relationship(n, k))
