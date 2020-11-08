# https://atcoder.jp/contests/abc181/tasks/abc181_c

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

for a in range(N):
    for b in range(a):
        for c in range(b):
            xa, ya = XY[a]
            xb, yb = XY[b]
            xc, yc = XY[c]

            xb -= xa
            yb -= ya

            xc -= xa
            yc -= ya

            if yc * xb == yb * xc:
                print('Yes')
                exit()

print('No')
