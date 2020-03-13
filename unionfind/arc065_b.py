class UnionFind:
    def __init__(self, elements):
        self.elements = elements

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        parent = self.elements[a]
        if parent < 0:
            return a
        self.elements[a] = self.find(parent)
        return self.elements[a]

    def unite(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        # already same union
        if a_parent == b_parent:
            return

        self.elements[a_parent] += self.elements[b_parent]
        self.elements[b_parent] = a_parent


N, K, L = map(int, input().split())
road_union = UnionFind([-1 for i in range(N)])
for _ in range(K):
    a, b = map(int, input().split())
    road_union.unite(a - 1, b - 1)

train_union = UnionFind([-1 for i in range(N)])
for _ in range(L):
    a, b = map(int, input().split())
    train_union.unite(a - 1, b - 1)

ma = dict()
for i in range(N):
    p = (road_union.find(i), train_union.find(i))
    ma[p] = ma.get(p, 0) + 1

for i in range(N):
    p = (road_union.find(i), train_union.find(i))
    print(ma[p], end=' ')
