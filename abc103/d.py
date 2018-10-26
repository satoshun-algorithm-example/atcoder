def island(a, n):
    splits = []
    a = sorted(a, key=lambda e: e[1])
    for i in range(0, len(a)):
        aa = a[i]
        included = False
        target = range(aa[0] + 1, aa[1])
        for s in splits:
            if s in target:
                included = True
                break
        if included:
            continue
        splits += [aa[1]]
    return len(splits)

n, m = map(int, input().split())
a = []
for _ in range(m):
    aa, bb = map(int, input().split())
    a += [(aa, bb)]
print(island(a, n))
