import sys


def main():
    n, m = map(int, input().split())
    op = []
    for _ in range(m):
        a, b = input().split()
        op.append([a, int(b)])

    dp = [[sys.maxsize] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            o = op[j]
            if o[0][i] == 'Y':
                dp[i][j] = min(dp[i][j], dp[i][j - 1], dp[i - 1][j - 1] + o[1])

    print(dp[-1][-1])


main()
