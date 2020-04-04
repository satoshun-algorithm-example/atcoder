# https://atcoder.jp/contests/abc161/tasks/abc161_d
from collections import deque

K = int(input())
ans = 0
count = 0
queue = deque()
for i in range(1, 10):
    queue.append(i)

while True:
    count += 1
    a = queue.popleft()
    if count == K:
        print(a)
        exit(0)

    for i in range(-1, 2):
        d = a % 10 + i
        if d < 0 or d > 9:
            continue
        queue.append(a * 10 + d)
