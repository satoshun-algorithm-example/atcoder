l = int(input())

n = 1
ii = 0
while True:
    n *= 2
    ii += 1
    if n > l:
        n //= 2
        break

for i in range(0, ii):
    print(i, i+1, 0)
    print(i, i+1, 2**i)


