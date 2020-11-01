X, Y, A, B = map(int, input().split())

ans = 0

while True:
    a = X * A
    b = X + B
    if a > b or a >= Y:
        break

    X = X * A
    ans += 1

d = Y - X
ans += ((d - 1) // B)

print(ans)
