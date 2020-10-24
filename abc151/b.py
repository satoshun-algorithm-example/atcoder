N, K, M = map(int, input().split())
a = map(int, input().split())

result = N * M - sum(a)
if result <= 0:
    print(0)
elif result <= K:
    print(result)
else:
    print(-1)
