def red_and_green_apples(X, Y, A, B, C, P, Q, R):
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)

    P = P[:X]
    Q = Q[:Y]
    q = P + Q + R
    q.sort(reverse=True)

    return sum(q[:X + Y])


X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

print(red_and_green_apples(X, Y, A, B, C, P, Q, R))

# red_and_green_apples(
#     1, 2, 2, 2, 1,
#     [2, 4],
#     [5, 1],
#     [3],
# )
#
# red_and_green_apples(
#     2, 2, 2, 2, 2,
#     [8, 6],
#     [9, 1],
#     [2, 1],
# )
