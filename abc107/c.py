n, k = map(int, input().split())
xs = list(map(int, input().split()))

ml = len(xs) - 1
center = ml
for i in range(center + 1):
    if xs[i] >= 0:
        if xs[i] == 0:
            center = i
            break
        center = i - 1
        break

t = 1000000000
cur = center
# left
while cur > 0:
    if ml - cur + 1 >= k:
        tt = abs(xs[cur])
        tt += abs(xs[cur] - xs[cur + k - 1])
        if tt <= t:
            t = tt
    cur -= 1

# only left
if center >= k:
    tt = 0
    tt += abs(xs[center-k] - xs[center])
    if tt <= t:
        t = tt

# only right
if ml - center >= k:
    tt = 0
    tt += abs(xs[center] - xs[center+k])
    if tt <= t:
        t = tt

if t == 1000000000:
    print(0)
    exit(0)

print(t)
