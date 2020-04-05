# https://atcoder.jp/contests/abc160/tasks/abc160_c

K, N = map(int, input().split())
A = list(map(int, input().split()))

max_distance = -1
for i in range(len(A)):
    if len(A) - 1 == i:
        max_distance = max(max_distance, (K - A[i]) + A[0])
    else:
        max_distance = max(max_distance, A[i + 1] - A[i])

print(K - max_distance)
