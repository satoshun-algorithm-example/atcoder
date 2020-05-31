M = 10 ** 18
N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit(0)

res = 1
for a in A:
    res *= a
    if res > M:
        print(-1)
        exit(0)

print(res)
