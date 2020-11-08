import sys

a, b, c, d = map(int, input().split())

m = -sys.maxsize
for i in range(2):
    for j in range(2):
        if i == 0:
            x = a
        else:
            x = b

        if j == 0:
            y = c
        else:
            y = d

        m = max(m, x * y)

print(m)
