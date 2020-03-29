# https://atcoder.jp/contests/abc157/tasks/abc157_e

N = int(input())
S = list(input())
Q = int(input())

for _ in range(Q):
    TYPE, Q1, Q2 = input().split()
    if TYPE == '1':
        Q1 = int(Q1)
        S[Q1 - 1] = Q2
    else:
        Q1, Q2 = int(Q1), int(Q2)
        print(len(set(S[Q1 - 1:Q2])))
