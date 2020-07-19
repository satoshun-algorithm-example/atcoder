n, m = map(int, input().split())

ac = [False for _ in range(n)]
wa = [0 for _ in range(n)]

for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == 'AC':
        ac[p - 1] = True
    if s == 'WA' and not ac[p - 1]:
        wa[p - 1] += 1

r1 = sum(ac)
r2 = sum(wa[i] if ac[i] else 0 for i in range(n))

print(r1, r2)
