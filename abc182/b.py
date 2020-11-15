N = int(input())
A = list(map(int, input().split()))

n = -1
gcd = 0
for i in range(2, max(A) + 1):
    g = sum(j % i == 0 for j in A)

    if g > n:
        n = g
        gcd = i

print(gcd)
