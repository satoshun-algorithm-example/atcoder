N = int(input())
A = list(map(int, input().split()))

p = [(a, i) for i, a in enumerate(A)]
p.sort(reverse=True)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    pa = p[i][0]
    pi = p[i][1]

    for l in range(i + 1):
        dp[i + 1][l + 1] = max(dp[i + 1][l + 1], dp[i][l] + (pi - l) * pa)

        r = i - l
        d = (N - 1 - r) - pi
        dp[i + 1][l] = max(dp[i + 1][l], dp[i][l] + d * pa)

print(max(dp[N]))
