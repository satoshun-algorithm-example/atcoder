from collections import deque

h, w = map(int, input().split())

s = []

for i in range(h):
    s.append(list(input()))


def bfs(x, y):
    if s[y][x] == '#':
        return 0

    queue = deque()
    queue.appendleft([x, y])
    visited = dict()
    visited[(x, y)] = 0

    while queue:
        nx, ny = queue.pop()
        cur = visited[(nx, ny)]

        if nx - 1 >= 0 and (nx - 1, ny) not in visited:
            if s[ny][nx - 1] == '.':
                visited[(nx - 1, ny)] = cur + 1
                queue.appendleft((nx - 1, ny))

        if nx + 1 < w and (nx + 1, ny) not in visited:
            if s[ny][nx + 1] == '.':
                visited[(nx + 1, ny)] = cur + 1
                queue.appendleft((nx + 1, ny))

        if ny - 1 >= 0 and (nx, ny - 1) not in visited:
            if s[ny - 1][nx] == '.':
                visited[(nx, ny - 1)] = cur + 1
                queue.appendleft((nx, ny - 1))

        if ny + 1 < h and (nx, ny + 1) not in visited:
            if s[ny + 1][nx] == '.':
                visited[(nx, ny + 1)] = cur + 1
                queue.appendleft((nx, ny + 1))

    return max(visited.values())


result = 0
for i in range(h):
    for j in range(w):
        r = bfs(j, i)
        result = max(result, r)

print(result)
