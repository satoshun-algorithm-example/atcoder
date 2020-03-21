# https://atcoder.jp/contests/arc036/tasks/arc036_d

class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        self.parents[pb] = pa

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        v = self.parents[a]
        if v == a:
            return v
        self.parents[a] = self.find(v)
        return self.parents[a]


N, Q = map(int, input().split())
find = UnionFind([i for i in range(N * 2)])

for _ in range(Q):
    W, X, Y, Z = map(int, input().split())
    X = X - 1
    Y = Y - 1

    if W == 1:
        # 偶数
        if Z % 2 == 0:
            find.unite(X * 2, Y * 2)
            find.unite(X * 2 + 1, Y * 2 + 1)
        # 奇数
        else:
            find.unite(X * 2, Y * 2 + 1)
            find.unite(X * 2 + 1, Y * 2)
    else:
        if find.same(X * 2, Y * 2):
            print('YES')
        else:
            print('NO')
