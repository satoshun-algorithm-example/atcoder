# https://atcoder.jp/contests/abc181/tasks/abc181_b

N = int(input())

d = [0] * ((10 ** 6) + 2)

for _ in range(N):
    a, b = map(int, input().split())

    d[a] += 1
    d[b + 1] -= 1

for i in range(len(d) - 1):
    d[i + 1] += d[i]

ans = 0

for i in range(len(d)):
    ans += (d[i] * i)

print(ans)
