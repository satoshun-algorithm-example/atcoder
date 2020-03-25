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

deg = [0 for _ in range(N)]
to = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    deg[A - 1] += 1
    deg[B - 1] += 1
    union.unite(A - 1, B - 1)

for _ in range(K):
    A, B = map(int, input().split())
    to[A - 1].append(B - 1)
    to[B - 1].append(A - 1)

for i in range(N):
    ans = union.size(i) - 1 - deg[i]
    for u in to[i]:
        ans -= union.same(i, u)

    if i == N - 1:
        end = '\n'
    else:
        end = ' '
    print(ans, end=end)
