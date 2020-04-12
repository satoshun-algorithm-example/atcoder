# https://atcoder.jp/contests/abc161/tasks/abc161_d
from collections import deque

numbers = deque([i for i in range(1, 10)])
K = int(input())
k = 0
ans = 0

while K != k:
    n = numbers.popleft()
    if n % 10 == 0:
        numbers.append(n * 10)
        numbers.append(n * 10 + 1)
    elif n % 10 == 9:
        numbers.append(n * 10 + 8)
        numbers.append(n * 10 + 9)
    else:
        d = n % 10
        numbers.append(n * 10 + d - 1)
        numbers.append(n * 10 + d)
        numbers.append(n * 10 + d + 1)

    k += 1
    ans = n

print(ans)
