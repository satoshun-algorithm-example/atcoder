N = int(input())

ans = []

for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        ans.append(i)
        ans.append(N // i)

for i in sorted(ans):
    print(i)
