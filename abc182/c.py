N = int(input())

c = [0, 0, 0]

ns = str(N)
for i, s in enumerate(ns):
    c[int(s) % 3] += 1
