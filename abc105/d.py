from collections import defaultdict

n, m = map(int, input().split())
alist = list(map(int, input().split()))

c = 0
cnt = defaultdict(int)
cnt[0] = 1
s = 0
for i in range(n):
    s += alist[i]
    c += cnt[s%m]
    cnt[s%m] += 1

print(c)
