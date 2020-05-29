N, K = map(int, input().split())
N += 1

res = 0
s = [i for i in range(N)]

if K == 1:
    res += N
    K = 2

if N == 0:
    print(res)
    exit(0)

res += 1
minimum = sum(s[:K - 1])
maximum = sum(s[-K + 1:])

for i in range(K, N):
    minimum += s[i]
    maximum += s[-i + 1]
    res = (res + (maximum - minimum + 1)) % (10 ** 9 + 7)

print(res)
