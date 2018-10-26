def cracker(n, k):
    return 0 if k / n == 0 else 1

n, k = map(int, input().split())
print(cracker(n, k))
