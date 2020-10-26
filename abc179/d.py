N, K = map(int, input().split())

LR = []
S = set()
for _ in range(K):
    l, r = map(int, input().split())
    LR.append((l, r))

    for i in range(l, r + 1):
        S.add(i)

dp = [0 for _ in range(N + 10)]
dp[10] = 1

for i in range(11, N + 10):
    dp[i] = sum(dp[i - s] for s in S) % 998244353

print(dp[-1])
