import itertools

def combination(d):
    dd = [i for i in range(d)]
    return [itertools.combinations(dd, i) for i in range(1, d + 1)]

def all_green(d, g, ps, cs):
    # tood use int max value or other constant value
    min_count = 1000000
    for cc in combination(d):
        for c in cc:
            v = 0
            count = 0
            for ccc in c:
                v += cs[ccc]
                v += (ccc + 1) * 100 * ps[ccc]
                count += ps[ccc]
            if v >= g:
                if count < min_count:
                    min_count = count
                continue
            if count >= min_count:
                continue

            dd = [i if i not in c else None for i in range(d)]
            dd = list(filter(lambda x: x is not None, dd))
            for vvv in reversed(dd):
                for _ in range(ps[vvv]):
                    v += 100 * (vvv + 1)
                    count += 1
                    if v >= g:
                        if count < min_count:
                            min_count = count
                        break
                if count >= min_count:
                    break
    return min_count

d, g = map(int, input().split())
ps = []
cs = []
for _ in range(d):
    p, c = map(int, input().split())
    ps += [p]
    cs += [c]
print(all_green(d, g, ps, cs))
