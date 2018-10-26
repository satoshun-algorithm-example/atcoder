def cracker(n, k):
    return 0 if n % k == 0 else 1

n, k = map(int, input().split())
print(cracker(n, k))
