# https://atcoder.jp/contests/abc157/tasks/abc157_e
import bisect

N = int(input())
S = list(input())
Q = int(input())

acc = [[] for _ in range(26)]
for i in range(N):
    bisect.insort_left(acc[ord(S[i]) - ord('a')], i)

for _ in range(Q):
    TYPE, Q1, Q2 = input().split()
    if TYPE == '1':
        Q1 = int(Q1) - 1
        del acc[ord(S[Q1]) - ord('a')][bisect.bisect_left(acc[ord(S[Q1]) - ord('a')], Q1)]
        S[Q1] = Q2
        bisect.insort_left(acc[ord(S[Q1]) - ord('a')], Q1)

    else:
        Q1, Q2 = int(Q1) - 1, int(Q2)
        ans = 0
        for i in range(26):
            if not acc[i]:
                continue
            it = bisect.bisect_left(acc[i], Q1)
            if it != acc[i][-1] and it < Q2:
                ans += 1

        print(ans)
