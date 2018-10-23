def island(s, t, m):
    tt = []
    for i, j in zip(s, t):
        tt += [range(i, j)]
    i = 0
    while tt:
        i += 1
        ma = []
        for j in range(1, m + 1):
            can = []
            for iii, ttt in enumerate(tt):
                if j in ttt:
                    can += [iii]
            if len(ma) < len(can):
                ma = can
        for h in reversed(ma):
            del tt[h]
    return i

n, m = map(int, input().split())
a = []
b = []
for _ in range(m):
    aa, bb = map(int, input().split())
    a += [aa]
    b += [bb]

print(island(a, b, n))
