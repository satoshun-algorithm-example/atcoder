st = input()

s = 0
for i in range(len(st)):
    p = st[i]
    if not (p == 'B' or p == '?'):
        continue

    # ABC
    a1 = 0
    q1 = 0
    for l in range(0, i+1):
        if st[l] == 'A':
            a1 += 1
        if st[l] == '?':
            q1 += 1

    b2 = 0
    q2 = 0
    for r in range(i+1, len(st)):
        if st[r] == 'C':
            b2 += 1
        if st[r] == '?':
            q2 += 1
    s += a1 * b2 * 3**(q1+q2)

    # AB?
    s += a1 * q2 * 3**(q1+(q2-1))

    # ?BC
    s += q1 * b2 * 3**((q1-1)+q2)

    # ?B?
    s += q1 * q2 * 3**((q1-1)+(q2-1))

print(s)
