# https://atcoder.jp/contests/abc160/tasks/abc160_d
N, X, Y = map(int, input().split())

visited = set()

# special case: first advance
for i in range(N - 1):
    visited.add((i, i + 1))
visited.add((X - 1, Y - 1))

print(len(visited))

next_items = visited.copy()
for _ in range(N - 2):
    candidates = []

    for point in next_items:
        x, y = point

        if (x - 1, y) not in visited and x - 1 >= 0:
            visited.add((x - 1, y))
            candidates.append((x - 1, y))

        if (x + 1, y) not in visited and x + 1 != y:
            visited.add((x + 1, y))
            candidates.append((x + 1, y))

        if (x, y - 1) not in visited and x != y - 1:
            visited.add((x, y - 1))
            candidates.append((x, y - 1))

        if (x, y + 1) not in visited and y + 1 < N:
            visited.add((x, y + 1))
            candidates.append((x, y + 1))

    print(len(candidates))
    next_items = candidates
