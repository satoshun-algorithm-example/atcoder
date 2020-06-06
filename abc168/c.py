import math

A, B, H, M = map(int, input().split())

tm = M / 60.0 * 2 * math.pi
mx = B * math.cos(tm)
my = B * math.sin(tm)

th = (H * 60.0 + M) / 720 * 2 * math.pi
hx = A * math.cos(th)
hy = A * math.sin(th)

dx = hx - mx
dy = hy - my

print(math.sqrt(dx * dx + dy * dy))
