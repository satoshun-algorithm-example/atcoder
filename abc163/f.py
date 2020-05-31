N = int(input())
C = [c - 1 for c in map(int, input().split())]

AB = dict()
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    AB.setdefault(a, [])
    AB[a].append(b)

    AB.setdefault(b, [])
    AB[b].append(a)

for color in range(N):
    visited = set()


    def bfs(start, v):
        edges = AB[v]
        for edge in edges:
            if edge > start:
                p = (start, edge)
            else:
                p = (edge, start)

            if p not in visited:
                visited.add(p)
                bfs(start, edge)


    for vertex in range(N):
        if C[vertex] == color:
            visited.add((vertex, vertex))
            bfs(vertex, vertex)

    print(visited)
    print(len(visited))
