# https://atcoder.jp/contests/abc161/tasks/abc161_e
N, K, C = map(int, input().split())
S = input()

group = []
batu = 0
maru = 0
for i in range(len(S)):
    if S[i] == 'x':
        batu += 1
        if batu == C:
            batu = 0
            if maru != 0:
                group.append(maru)
                maru = 0
        continue
    if batu != 0:
        maru = maru << batu
        batu = 0
    maru = maru << 1
    maru += 1

group.append(maru)

maximum = []
for g in group:
    s = format(g, 'b')
    m = 0
    i = 0
    for c in s:
        if c == '1' and i <= 0:
            m += 1
            i = C
            continue
        i -= 1

    maximum.append(m)

if sum(maximum) > K:
    exit(0)

for i in range(len(group)):
    g = group[i]
    m = maximum[i]
    if format(g, 'b').count("1") != m:
        print(g, m)
