# https://atcoder.jp/contests/abc157/tasks/abc157_d

class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def find(self, a):
        pa = self.parents[a]
        if pa < 0:
            return a
        self.parents[a] = self.find(pa)
        return self.parents[a]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        self.parents[pa] += self.parents[pb]
        self.parents[pb] = pa

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def size(self, a):
        return -self.parents[self.find(a)]


N, M, K = map(int, input().split())
union = UnionFind([-1 for i in range(N)])

m = [0 for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    m[A - 1] += 1
    m[B - 1] += 1
    union.unite(A - 1, B - 1)

for i in range(N):
    m[i] = union.size(i) - 1 - m[i]

for _ in range(K):
    A, B = map(int, input().split())
    m[A - 1] -= union.same(A - 1, B - 1)
    m[B - 1] -= union.same(A - 1, B - 1)

for j, ans in enumerate(m):
    print(ans, end=' ')
