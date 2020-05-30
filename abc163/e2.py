N = int(input())
A = list(map(int, input().split()))

# dp[n][k]: nは現在使っている個数、kは左から詰めた個数
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

p = [(a, i) for i, a in enumerate(A)]
p.sort(reverse=True)

for i in range(N):
    pi = p[i][1]

    for l in range(i + 1):
        # add to left
        dp[i + 1][l + 1] = max(dp[i + 1][l + 1], dp[i][l] + (pi - l) * A[pi])

        r = i - l
        # add to right
        dp[i + 1][l] = max(dp[i + 1][l], dp[i][l] + ((N - r - 1) - pi) * A[pi])

print(max(dp[N]))
