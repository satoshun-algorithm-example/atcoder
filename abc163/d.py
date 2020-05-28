from itertools import combinations

N, K = map(int, input().split())
N += 1

res = 1
s = [i for i in range(N)]

for i in range(K, N):
    c = set(map(sum, combinations(s, i)))
    res += len(c)

print(res)
