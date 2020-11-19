x, y = map(int, input().split())

for a in range(x + 1):
    b = x - a
    if (a * 2 + b * 4) == y:
        print('Yes')
        exit()

print('No')
