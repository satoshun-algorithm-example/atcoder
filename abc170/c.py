import sys

X, N = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

a = [i for i in range(102) if i not in p]

ans = -1
diff = sys.maxsize
for i in a:
    if abs(i - X) < diff:
        diff = abs(i - X)
        ans = i

print(ans)
