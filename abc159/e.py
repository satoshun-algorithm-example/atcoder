# https://atcoder.jp/contests/abc159/tasks/abc159_e

H, W, K = map(int, input().split())

cum = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for h in range(H):
    count = 0
    s = input()
    for w, c in enumerate(s):
        count += c == '1'
        cum[h + 1][w + 1] = count

sum_count = 0


def search(left, right, top, bottom):
    global sum_count

    k = 0
    for i in range(top + 1, bottom + 1):
        k += (cum[i][right] - cum[i][left])

    print(k, left, right, top, bottom)
    if k <= K:
        return

    sum_count += 1

    # (x, y)
    good = k // 2
    point = (-1, -1)
    diff = good

    for y in range(top + 1, bottom + 1):
        candidate = sum(cum[i][right] - cum[i][left] for i in range(top + 1, y + 1))
        if abs(good - candidate) < diff:
            diff = abs(good - candidate)
            point = (-1, y)

    for x in range(left + 1, right + 1):
        candidate = sum(cum[i][x] - cum[i][left] for i in range(top + 1, bottom + 1))
        if abs(good - candidate) < diff:
            diff = abs(good - candidate)
            point = (x, -1)

    if point[0] != -1:
        search(left, point[0], top, bottom)
        search(point[0], right, top, bottom)
    else:
        search(left, right, top, point[1])
        search(left, right, point[1], bottom)


search(0, W, 0, H)

print(sum_count)
