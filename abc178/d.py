S = int(input())

mod = 10 ** 9 + 7

a = [0] * (S + 1)
a[0] = 1

for i in range(3, S + 1):
    a[i] = sum(a[0:i - 2]) % mod

print(a[S])
