S = input()

d = [0] * 10
for s in S:
    d[int(s)] += 1

for r in range(8, 1000, 8):
    ok = True

    if len(S) == 2 and r < 10:
        continue

    if len(S) == 3 and r < 100:
        continue

    count = [0] * 10
    for s in str(r):
        count[int(s)] += 1

    for i in range(10):
        if count[i] > d[i]:
            ok = False
            break

    if ok:
        print('Yes')
        exit()

print('No')
