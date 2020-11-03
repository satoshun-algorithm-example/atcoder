import sys

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
C = [[0] * N for _ in range(N)]

for i in range(N):
    xi, yi, zi = P[i]

    for j in range(N):
        xj, yj, zj = P[j]
        C[i][j] = abs(xj - xi) + abs(yj - yi) + max(0, zj - zi)

# dp[n][j] n = 訪問済み集合, j = 現在地
dp = [[sys.maxsize] * N for _ in range(1 << N)]
dp[0][0] = 0

for s in range(1 << N):
    for i in range(N):
        bit = 1 << i
        if (s & bit) != 0:
            for j in range(N):
                dp[s][i] = min(dp[s][i], dp[s - (s & bit)][j] + C[j][i])

print(dp[(1 << N) - 1][0])
