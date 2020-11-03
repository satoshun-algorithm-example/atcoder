N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0

for (a, b) in AB:
    ans += (b - a + 1) * (b + a) // 2

print(ans)
