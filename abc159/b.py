# https://atcoder.jp/contests/abc159/tasks/abc159_b

S = input()
n = len(S)
s1 = S[:(n - 1) // 2]
s2 = S[((n + 3) // 2):-1]

if S == S[::-1] and s1 == s1[::-1] and s2 == s2[::-1]:
    print('Yes')
else:
    print('No')
