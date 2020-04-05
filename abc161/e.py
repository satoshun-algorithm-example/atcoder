# https://atcoder.jp/contests/abc161/tasks/abc161_e
N, K, C = map(int, input().split())
S = input()

i = 0
left = []
while i < N and len(left) < K:
    if S[i] == 'o':
        left.append(i)
        i += (C + 1)
        continue
    i += 1

i = N - 1
right = []
while i >= 0 and len(right) < K:
    if S[i] == 'o':
        right.append(i)
        i -= (C + 1)
        continue
    i -= 1

n = len(left)
for i in range(n):
    if left[i] == right[n - i - 1]:
        print(left[i] + 1)
