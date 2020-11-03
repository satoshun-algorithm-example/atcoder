# https://atcoder.jp/contests/abc180/tasks/abc180_e
import sys

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
C = [[0] * N for _ in range(N)]

for i in range(N):
    xi, yi, zi = P[i]

    for j in range(N):
        xj, yj, zj = P[j]
        C[i][j] = abs(xi - xj) + abs(yi - yj) + max(0, zj - zi)

dp = [[sys.maxsize] * N for _ in range(1 << N)]
dp[0][0] = 0

for s in range(1 << N):
    for i in range(N):
        if (1 << i) & s:
            for j in range(N):
                dp[s][i] = min(dp[s][i], dp[s - (1 << i)][j] + C[j][i])

print(dp[(1 << N) - 1][0])
