def minimum(a1, a2, a3):
    a = sorted([a1, a2, a3])
    return abs(a[0] - a[1]) + abs(a[1] - a[2])

a, b, c = map(int, input().split())
print(minimum(a, b, c))
