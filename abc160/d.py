# https://atcoder.jp/contests/abc160/tasks/abc160_d
N, X, Y = map(int, input().split())

visited = set()

# special case: first advance
for i in range(N - 1):
    visited.add((i, i + 1))
visited.add((X - 1, Y - 1))

print(len(visited))

for _ in range(N - 2):
    total = 0

    for point in visited.copy():
        x, y = point

        if (x - 1, y) not in visited and x - 1 >= 0:
            visited.add((x - 1, y))
            total += 1

        if (x + 1, y) not in visited and x + 1 != y:
            visited.add((x + 1, y))
            total += 1

        if (x, y - 1) not in visited and x != y - 1:
            visited.add((x, y - 1))
            total += 1

        if (x, y + 1) not in visited and y + 1 < N:
            visited.add((x, y + 1))
            total += 1

    print(total)
