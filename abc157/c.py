# https://atcoder.jp/contests/abc157/tasks/abc157_c

N, M = map(int, input().split())
c = [-1 for _ in range(N)]

for _ in range(M):
    S, C = map(int, input().split())
    if c[S - 1] != -1 and c[S - 1] != C:
        print(-1)
        exit(0)
    c[S - 1] = C

if N == 1 and c[0] == 0:
    print(0)
    exit(0)

if N == 1 and c[0] == -1:
    print(0)
    exit(0)

if c[0] == 0:
    print(-1)
    exit(0)

s = ""
for i, a in enumerate(c):
    if i == 0:
        s += str(max(a, 1))
    else:
        s += str(max(a, 0))

print(s)
