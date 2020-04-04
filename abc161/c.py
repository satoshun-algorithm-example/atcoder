# https://atcoder.jp/contests/abc161/tasks/abc161_c
N, K = map(int, input().split())

a = N % K

print(min(a, abs(a - K)))
