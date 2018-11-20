n, m = map(int, input().split())
alist = list(map(int, input().split()))

ca = {0: 0}
for i, a in enumerate(alist):
    ca[i+1] = sum(alist[0:i+1]) % m

c = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        s = ca[j] - ca[i-1]
        if s % m == 0:
            c += 1
print(c)
