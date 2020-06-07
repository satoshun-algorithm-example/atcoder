N, M = map(int, input().split())

AB = dict()

for _ in range(M):
    a, b = map(int, input().split())
    AB.setdefault(a, [])
    AB[a].append(b)

    AB.setdefault(b, [])
    AB[b].append(a)

a = [-1 for _ in range(N + 1)]

a[1] = 0
current = 1
pos = [1]

while True:
    next_pos = []

    for p in pos:
        for n in AB[p]:
            if a[n] == -1:
                a[n] = p
                next_pos.append(n)

    pos = next_pos
    if not pos:
        break

if -1 in a[2:]:
    print('No')
else:
    print('Yes')
    for i in a[2:]:
        print(i)
