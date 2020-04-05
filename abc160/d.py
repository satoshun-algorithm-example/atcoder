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
print(len(a))

for i in range(1, N - 1):
    b = set()
    for n in a:
        # last
        if n[1] == N - 1:
            continue

        if n[1] == X:
            if (n[0], Y) not in total:
                total.add((n[0], Y))
                b.add((n[0], Y))

        if (n[0], n[1] + 1) not in total:
            total.add((n[0], n[1] + 1))
            b.add((n[0], n[1] + 1))

    a = b
    print(len(a))
