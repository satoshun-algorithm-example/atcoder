S = input()

if len(S) == 1:
    if int(S) == 8:
        print('Yes')
    else:
        print('No')
    exit()

if len(S) == 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

s2 = [0] * 10
for s in S:
    s2[int(s)] += 1

for target in range(112, 1000, 8):
    s1 = [0] * 10
    for s in str(target):
        s1[int(s)] += 1

    ok = True
    for i in range(10):
        if s1[i] > s2[i]:
            ok = False
            break

    if ok:
        print('Yes')
        exit()

print('No')
