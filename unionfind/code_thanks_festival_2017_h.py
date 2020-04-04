class UnionFind:
    def __init__(self, parents):
        self.parents = parents

    def find(self, a):
        pa = self.parents[a]
        if pa == a:
            return pa
        self.parents[a] = self.find(a)
        return self.parents[a]

    def unite(self, a, b, count):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        self.parents[pa] = pb


N, M = map(int, input().split())
