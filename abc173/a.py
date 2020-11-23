n = int(input())

n = n % 1000
if n:
    print(1000 - n)
else:
    print(0)
