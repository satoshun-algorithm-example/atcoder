# https://atcoder.jp/contests/abc158/tasks/abc158_d

S = input()
Q = int(input())

for _ in range(Q):
    query = input()
    if query[0] == '1':
        S = S[::-1]
    else:
        if query[2] == '1':
            S = query[4] + S
        else:
            S = S + query[4]

print(S)
