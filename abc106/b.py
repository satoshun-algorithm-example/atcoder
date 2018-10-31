def _105(n):
    b = 0
    for i in range(105, n + 1, 2):
        ii = i
        l = []
        for j in range(2, i + 1):
            while True:
                if ii % j == 0:
                    l += [j]
                    ii /= j
                else:
                    break
        if len(l) == 3:
            if len(set(l)) == 3:
                b += 1
        if len(l) == 4:
            if len(set(l)) == 2:
                l.remove(set(l).pop())
                if len(l) == 3 or len(l) == 1:
                    b += 1
    return b

print(_105(int(input())))
