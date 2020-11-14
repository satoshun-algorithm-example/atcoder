N = int(input())

mod = 10 ** 9 + 7

ans = (10 ** N - (9 ** N + 9 ** N - 8 ** N)) % mod
print(ans)
