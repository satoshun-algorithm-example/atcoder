def modulo(n, a):
    return sum(a) - n

n = int(input())
a = map(int, input().split())
print(modulo(n, a))
