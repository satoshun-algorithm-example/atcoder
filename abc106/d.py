n, m, q = map(int, input().split())

ls = []
for _ in range(m):
    ls += [list(map(int, input().split()))]
qs = []
for _ in range(q):
    a, b = list(map(int, input().split()))
    qs += [range(a, b + 1)]

for qq in qs:
    c = 0
    for ll in ls:
        if ll[0] in qq and ll[1] in qq:
            c += 1
    print(c)
