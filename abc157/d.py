# https://atcoder.jp/contests/abc157/tasks/abc157_d

class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def find(self, a):
        pa = self.parents[a]
        if pa == a:
            return pa
        self.parents[a] = self.find(pa)
        return self.parents[a]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        self.parents[pa] = pb

    def same(self, a, b):
        return self.find(a) == self.find(b)


N, M, K = map(int, input().split())
union = UnionFind([i for i in range(N)])

m = [[i != j for i in range(N)] for j in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    m[A - 1][B - 1] = 0
    m[B - 1][A - 1] = 0
    union.unite(A - 1, B - 1)

for _ in range(K):
    A, B = map(int, input().split())
    m[A - 1][B - 1] = 0
    m[B - 1][A - 1] = 0

for j, row in enumerate(m):
    ans = 0
    for i, e in enumerate(row):
        if e == 0:
            continue
        ans += union.same(i, j)

    print(ans, end=' ')
