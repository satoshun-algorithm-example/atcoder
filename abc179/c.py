N = int(input())

result = 0
for a in range(1, N):
    for b in range(1, N):
        r = a * b
        if r >= N:
            break

        result += 1

print(result)
