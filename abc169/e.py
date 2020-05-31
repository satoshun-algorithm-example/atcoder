N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

res = 0
if N % 2 == 1:
    center = N // 2
    a = A[center]
    b = B[center]
    res = b - a + 1
else:
    center = N // 2
    a = (A[center] + A[center]) / 2
    b = (B[center] + B[center]) / 2
    res = int(b - a) * 2 + 1

print(res)
