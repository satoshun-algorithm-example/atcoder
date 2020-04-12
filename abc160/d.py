# https://atcoder.jp/contests/abc160/tasks/abc160_d
N, X, Y = map(int, input().split())
X = X - 1
Y = Y - 1

# check distance 1
a = set()
for n in range(N - 1):
    a.add((n, n + 1))
a.add((X, Y))
total = a.copy()


def add(b, p1, p2):
    if p1 == p2:
        return

    if (p1, p2) in total:
        return

    b.add((p1, p2))
    total.add((p1, p2))
    total.add((p2, p1))


print(len(a))

for i in range(1, N - 1):
    b = set()
    for n in a:
        if n[1] != 0:
            add(b, n[0], n[1] - 1)

        if n[1] != N - 1:
            add(b, n[0], n[1] + 1)

        if n[1] == X:
            add(b, n[0], Y)

        if n[1] == Y:
            add(b, n[0], X)

    a = b
    print(len(a))
