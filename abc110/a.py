def maximize_the_formula(a, b, c):
    l = sorted([a, b, c])
    return l[2] * 10 + l[1] + l[0]

a, b, c = map(int, input().split())
print(maximize_the_formula(a, b, c))
