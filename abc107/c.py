def candles(n, k, xs):
    mini = 1000000000000000

    def _hoge(i, filled, dis, is_left, can_rotate):
        nonlocal mini

        ri = i + 1
        li = i - 1

        if i < 0 or len(xs) == i:
            return
        if not filled:
            dis += abs(xs[i])
        elif is_left:
            dis += abs(xs[i] - xs[i + 1])
        else:
            dis += abs(xs[i] - xs[i - 1])
        if i not in filled:
            filled = list(filled)
            filled += [i]
            if len(filled) == k:
                if mini > dis:
                    mini = dis
                return

        if mini < dis:
            return

        if is_left:
            _hoge(li, filled, dis, is_left, can_rotate)
        else:
            _hoge(ri, filled, dis, is_left, can_rotate)
        if can_rotate:
            if is_left:
                _hoge(ri, filled, dis, False, False)
            else:
                _hoge(li, filled, dis, True, False)

    ri = min(filter(lambda x: x >= 0, xs))
    _hoge(xs.index(ri), [], 0, False, True)

    li = max(filter(lambda x: x <= 0, xs))
    _hoge(xs.index(li), [], 0, True, True)

    return mini

n, k = map(int, input().split())
xs = list(map(int, input().split()))
print(candles(n, k, xs))
