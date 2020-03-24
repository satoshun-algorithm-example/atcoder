# https://atcoder.jp/contests/abc157/tasks/abc157_b

A = [list(map(int, input().split())) for a in range(3)]
N = int(input())

for _ in range(N):
    B = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == B:
                A[i][j] = -1

is_bingo = False
is_bingo = is_bingo or (A[0][0] == -1 and A[0][1] == -1 and A[0][2] == -1)
is_bingo = is_bingo or (A[1][0] == -1 and A[1][1] == -1 and A[1][2] == -1)
is_bingo = is_bingo or (A[2][0] == -1 and A[2][1] == -1 and A[2][2] == -1)
is_bingo = is_bingo or (A[0][0] == -1 and A[1][0] == -1 and A[2][0] == -1)
is_bingo = is_bingo or (A[0][1] == -1 and A[1][1] == -1 and A[2][1] == -1)
is_bingo = is_bingo or (A[0][2] == -1 and A[1][2] == -1 and A[2][2] == -1)
is_bingo = is_bingo or (A[0][0] == -1 and A[1][1] == -1 and A[2][2] == -1)
is_bingo = is_bingo or (A[0][2] == -1 and A[1][1] == -1 and A[2][0] == -1)

if is_bingo:
    print('Yes')
else:
    print('No')
