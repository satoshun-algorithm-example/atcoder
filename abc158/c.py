A, B = map(int, input().split())

for i in range(10000):
    a = int(i * 0.08)
    b = int(i * 0.1)

    if A == a and B == b:
        print(i)
        exit(0)

print(-1)
