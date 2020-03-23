# https://atcoder.jp/contests/abc159/tasks/abc159_a

N, M = map(int, input().split())
count = 0

count += M * (M - 1)
count += N * (N - 1)

print(count // 2)
