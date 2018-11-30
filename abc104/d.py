st = input()
wa = 10**9 + 7

s = 0

a1 = 0
q1 = 0

b2 = st[1:].count('C')
q2 = st[1:].count('?')

for i in range(1, len(st)):
    bp = st[i-1]
    p = st[i]
    if p == 'A':
        pass
    if p == 'B':
        pass
    if p == 'C':
        b2 -= 1
    if p == '?':
        q2 -= 1
    if bp == 'A':
        a1 += 1
    if bp == 'B':
        pass
    if bp == 'C':
        pass
    if bp == '?':
        q1 += 1
    if not (p == 'B' or p == '?'):
        continue

    # ABC
    s += a1 * b2 * 3**(q1+q2)

    # AB?
    s += a1 * q2 * 3**(q1+(q2-1))

    # # ?BC
    s += q1 * b2 * 3**((q1-1)+q2)

    # # ?B?
    s = (s + q1 * q2 * 3**((q1-1)+(q2-1))) % wa

print(int(s))
