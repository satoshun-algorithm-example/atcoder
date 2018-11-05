def ruined_square(x1, y1, x2, y2):
    if x1 == x2 and y1 > y2:
        d = abs(y1 - y2)
        return (x1 + d) + ' ' + y2 + ' ' + (x1 + d) + ' ' + y1
    if x1 == x2 and y1 < y2:
        d = abs(y1 - y2)
        return _f(x1 - d, y2, x1 - d, y1)
    if x1 > x2 and y1 == y2:
        d = abs(x1 - x2)
        return x2 + ' ' + (y2 - d) + ' ' + x1 + ' ' + (y2 - d)
    if x1 < x2 and y1 == y2:
        d = abs(x1 - x2)
        return x2 + ' ' + (y2 + d) + ' ' + x1 + ' ' + (y2 + d)

def _f(x3, y3, x4, y4):
    return '{} {} {} {}'.format(x3, y3, x4, y4)

x1, y1, x2, y2 = map(int, input().split())
print(ruined_square(x1, y1, x2, y2))
