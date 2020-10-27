import math

N = int(input())
x = list(map(int, input().split()))

print(sum(abs(i) for i in x))
print(math.sqrt(sum(i * i for i in x)))
print(max(abs(i) for i in x))
