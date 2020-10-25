N = int(input())

d = []
for _ in range(N):
    a, b = map(int, input().split())
    d.append((a, b))

go_to_jail = False
s = 0
for (a, b) in d:
    if a == b:
        s += 1
    else:
        s = 0

    if s == 3:
        go_to_jail = True
        break

if go_to_jail:
    print("Yes")
else:
    print("No")
