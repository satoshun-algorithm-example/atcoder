# https://atcoder.jp/contests/abc162/tasks/abc162_d

N = int(input())
S = input()


def colors(target, a, b):
    for i in range(N):
        for j in range(i + 1, N):
            if S[i] == a and S[j] == b:
                target[i] += 1


rg = [0 for _ in range(N)]
colors(rg, 'R', 'G')
gr = [0 for _ in range(N)]
colors(gr, 'G', 'R')

gb = [0 for _ in range(N)]
colors(rg, 'G', 'B')
bg = [0 for _ in range(N)]
colors(gr, 'B', 'G')

rb = [0 for _ in range(N)]
colors(rg, 'R', 'B')
br = [0 for _ in range(N)]
colors(gr, 'B', 'R')

ans = 0
for i in range(N):
    if S[i] == 'B':
        for j in range(i + 1, N):
            ans += rg[j]
            ans += gr[j]

            k = j + j - i
            if k >= N:
                continue
            if S[i] == 'B' and S[j] == 'R' and S[k] == 'G':
                ans -= 1
            if S[i] == 'B' and S[j] == 'G' and S[k] == 'R':
                ans -= 1

    if S[i] == 'R':
        for j in range(i + 1, N):
            ans += gb[j]
            ans += bg[j]

            k = j + j - i
            if k >= N:
                continue
            if S[i] == 'R' and S[j] == 'G' and S[k] == 'B':
                ans -= 1
            if S[i] == 'R' and S[j] == 'B' and S[k] == 'G':
                ans -= 1

    if S[i] == 'G':
        for j in range(i + 1, N):
            ans += rb[j]
            ans += br[j]

            k = j + j - i
            if k >= N:
                continue
            if S[i] == 'G' and S[j] == 'R' and S[k] == 'B':
                ans -= 1
            if S[i] == 'G' and S[j] == 'B' and S[k] == 'R':
                ans -= 1

print(ans)
