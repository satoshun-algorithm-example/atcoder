# https://atcoder.jp/contests/abc157/tasks/abc157_d

N, M, K = map(int, input().split())

m = [[i != j for i in range(N)] for j in range(N)]

for _ in range(M + K):
    A, B = map(int, input().split())
    m[A - 1][B - 1] = 0 
    m[B - 1][A - 1] = 0

for i in m:
    print(sum(i), end=' ')
