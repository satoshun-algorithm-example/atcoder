from collections import Counter

n = int(input())
vs = input().split()

xs = [v for v in vs[::2]]
x = Counter(xs).most_common()

ys = [v for v in vs[1::2]]
y = Counter(ys).most_common()

if x[0][0] != y[0][0]:
    d = n - x[0][1] - y[0][1]
    print(d)
else:
    if len(x) == 1:
        print(n // 2)
    else:
        d1 = n - x[0][1] - y[1][1]
        d2 = n - x[1][1] - y[0][1]
        if d1 > d2:
            print(d2)
        else:
            print(d1)
