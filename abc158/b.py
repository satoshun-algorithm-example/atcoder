N, A, B = map(int, input().split())

base = A + B
count = (N // base)
remain = min(A, N % base)

print(A * count + remain)
