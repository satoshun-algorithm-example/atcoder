# https://atcoder.jp/contests/abc162/tasks/abc162_d

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if j - i == k - j:
                continue

            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans += 1

print(ans)
