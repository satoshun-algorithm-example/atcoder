n = int(input())
vs = input().split()

vs1 = [vs[i] for i in range(0, len(vs), 2)]
vs2 = [vs[i] for i in range(1, len(vs), 2)]

m1 = 0
i1 = -1
m2 = 0
i2 = -1
ccc = 0
for value in vs1:
    ccc += 1
    count = vs1.count(value)
    if count > m1:
        i2 = i1
        m2 = m1
        i1 = value
        m1 = count

m3 = 0
i3 = -1
m4 = 0
i4 = -1
ccc2 = 0
for value in vs2:
    ccc2 += 1
    count = vs2.count(value)
    if count > m3:
        i4 = i3
        m4 = m3
        i3 = value
        m3 = count

if i1 != i3:
    print((ccc - m1) + (ccc2 - m3))
else:
    if m2 > m4:
        print((ccc - m2) + (ccc2 - m3))
    else:
        print((ccc - m1) + (ccc2 - m4))
