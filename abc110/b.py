def dimensional_world_tale(x, y, xs, ys):
    xs = sorted(xs)
    maxx = xs[-1]
    if not(x < maxx <= y):
        return "War"
    ys = sorted(ys)
    miny = ys[0]
    if not(x < miny <= y):
        return "War"
    if not(maxx < miny):
        return "War"
    return "No War"

n, m, x, y = map(int, input().split())
xs = map(int, input().split())
ys = map(int, input().split())
print(dimensional_world_tale(x, y, xs, ys))
