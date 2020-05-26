# https://atcoder.jp/contests/abc161/tasks/abc161_e

N, K, C = map(int, input().split())
S = input()

left = []
i = 0
while K > len(left):
    while True:
        if S[i] == 'o':
            left.append(i)
            i += C + 1
            break
        i += 1

right = []
i = N - 1
while K > len(right):
    while True:
        if S[i] == 'o':
            right.append(i)
            i -= (C + 1)
            break
        i -= 1

right.reverse()

ans = 0
for i in range(K):
    if left[i] == right[i]:
        print(left[i] + 1)
