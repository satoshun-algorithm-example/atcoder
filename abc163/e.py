N = int(input())
A = list(map(int, input().split()))

move = [0 for _ in range(N)]

for i in range(1, N):
    pos = i
    for j in range(i - 1, -1, -1):
        distance = pos - j
        a1 = abs(move[pos] * A[pos]) + abs(move[j] * A[j])
        a2 = abs((move[pos] - distance) * A[pos]) + abs((move[j] + distance) * A[j])
        if a2 > a1:
            A[pos], A[j] = A[j], A[pos]
            move[pos] -= distance
            move[j] += distance
            move[pos], move[j] = move[j], move[pos]

            pos = j

print(sum(A[i] * abs(move[i]) for i in range(N)))
