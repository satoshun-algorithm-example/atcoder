# https://atcoder.jp/contests/abc160/tasks/abc160_c

K, N = map(int, input().split())
A = list(map(int, input().split()))
A.append(A[0] + K)

max_distance = -1
for i in range(len(A) - 1):
    max_distance = max(max_distance, A[i + 1] - A[i])

print(K - max_distance)
