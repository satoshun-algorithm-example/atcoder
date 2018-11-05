def ruined_square(x1, y1, x2, y2):
    x = x2
    y = y2
    dx = x2 - x1
    dy = y2 - y1

    dx, dy = -dy, dx
    x += dx
    y += dy
    print("{} {} ".format(x, y), end = "")

    dx, dy = -dy, dx
    x += dx
    y += dy
    print("{} {}".format(x, y))

x1, y1, x2, y2 = map(int, input().split())
ruined_square(x1, y1, x2, y2)
