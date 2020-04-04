# https://atcoder.jp/contests/abc161/tasks/abc161_b
N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
limit = total / (4 * M)

count = 0
for a in A:
    count += (a >= limit)

if count >= M:
    print("Yes")
else:
    print("No")
