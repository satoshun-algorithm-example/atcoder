# https://atcoder.jp/contests/abc157/tasks/abc157_e
import bisect

N = int(input())
S = list(input())
Q = int(input())

acc = [[] for _ in range(26)]
for i in range(N):
    acc[ord(S[i]) - ord('a')].append(i)

for _ in range(Q):
    TYPE, Q1, Q2 = input().split()
    if TYPE == '1':
        Q1 = int(Q1) - 1
        target = acc[ord(S[Q1]) - ord('a')]
        del target[bisect.bisect_left(target, Q1)]
        S[Q1] = Q2
        bisect.insort_left(acc[ord(S[Q1]) - ord('a')], Q1)

    else:
        Q1, Q2 = int(Q1) - 1, int(Q2)
        ans = 0
        for i in range(26):
            target = acc[i]
            if not target:
                continue

            it = bisect.bisect_left(target, Q1)
            if len(target) <= it:
                continue
            if target[it] < Q2:
                ans += 1

        print(ans)
