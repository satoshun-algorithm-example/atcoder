# https://atcoder.jp/contests/arc097/tasks/arc097_b
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


N, M = map(int, input().split())
P = list(map(int, input().split()))

union = UnionFind([-1 for _ in range(N)])
for _ in range(M):
    a, b = map(int, input().split())
    union.unite(a - 1, b - 1)

answer = 0
for i in range(N):
    answer += union.same(P[i] - 1, i)

print(answer)
