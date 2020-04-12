# https://atcoder.jp/contests/abc162/tasks/abc162_c
from math import gcd

K = int(input())

ans = 0

for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += gcd(gcd(i, j), k)

print(ans)
