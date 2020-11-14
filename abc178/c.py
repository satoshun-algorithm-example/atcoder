N = int(input())

mod_n = 10 ** 9 + 7

ans = (9 ** N + 9 ** N - 8 ** N) % mod_n
ans = ((10 ** N) - ans) % mod_n

print(ans)
