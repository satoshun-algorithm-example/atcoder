N = int(input())
A = map(int, input().split())

sub = [0 for i in range(N)]

for a in A:
    sub[a - 1] += 1

for s in sub:
    print(s)
