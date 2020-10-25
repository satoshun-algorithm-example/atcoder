N = int(input())

ab = {}
for a in range(1, N):
    for b in range(1, N):
        r = a * b
        if r >= N:
            break

        ab[r] = ab.get(r, 0) + 1

result = 0
for c in range(1, N):
    result += ab.get(N - c)

print(result)
