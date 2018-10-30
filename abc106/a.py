def garden(x, y):
    return (x - 1) * (y - 1)

a, b = map(int, input().split())
print(garden(a, b))
