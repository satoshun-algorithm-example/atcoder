# https://atcoder.jp/contests/arc090/tasks/arc090_b

class Edge:
    def __init__(self, v, cost):
        self.v = v
        self.cost = cost


N, M = map(int, input().split())
visited = [False for _ in range(N + 1)]
edges = dict()
dist = dict()

for _ in range(M):
    L, R, D = map(int, input().split())

    edges[L] = edges.get(L, [])
    edges[L].append(Edge(R, D))
    edges[R] = edges.get(R, [])
    edges[R].append(Edge(L, -D))


def bfs(v, d) -> bool:
    if visited[v]:
        return dist[v] == d

    dist[v] = d
    visited[v] = True
    for e in edges.get(v, []):
        if not bfs(e.v, e.cost + d):
            return False

    return True


for i in range(1, N + 1):
    if visited[i]:
        continue
    dist[i] = 0
    if not bfs(i, 0):
        print('No')
        exit(0)

print('Yes')
