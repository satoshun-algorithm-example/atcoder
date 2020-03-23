# https://atcoder.jp/contests/abc159/tasks/abc159_d

N = int(input())
A = list(map(int, input().split()))

m = {}
for a in A:
    m[a] = m.get(a, 0) + 1

max_value = 0
for value in m.values():
    # nC2
    max_value += (value * (value - 1)) // 2

for a in A:
    value = m[a]
    old_value = (value * (value - 1)) // 2
    new_value = ((value - 1) * (value - 2)) // 2
    print(max_value + new_value - old_value)
