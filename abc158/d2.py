# https://atcoder.jp/contests/abc158/tasks/abc158_d

S = input()
Q = int(input())
T = ""

for _ in range(Q):
    query = input()
    ty = query[0]
    if ty == '1':
        S, T = T, S
    else:
        if query[2] == '1':
            T += query[4]
        else:
            S += query[4]

T = T[::-1]
print(T + S)
