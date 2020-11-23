H, W, K = map(int, input().split())

C = [list(input()) for _ in range(H)]

ans = 0
for w in range(2 ** W):
    for h in range(2 ** H):
        s = 0
        for i in range(W):
            for j in range(H):
                if (w & (1 << i)) and (h & (1 << j)):
                    s += C[j][i] == '#'

        ans += s == K

print(ans)
