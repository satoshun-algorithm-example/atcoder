N = int(input())

ab = [tuple(map(int, input().split())) for _ in range(N)]

c = [0] * (10 ** 6 + 2)
for (a, b) in ab:
    c[a] += 1
    c[b + 1] -= 1

for i in range(1, len(c)):
    c[i] += c[i - 1]

print(sum(c[i] * i for i in range(len(c))))
