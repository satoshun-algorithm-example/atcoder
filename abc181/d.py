S = input()

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")

    exit()

d = [0] * 10
for s in S:
    d[int(s)] += 1

for r in range(112, 1000, 8):
    ok = True

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
