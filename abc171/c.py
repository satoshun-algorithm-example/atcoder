n = int(input())

ans = ''
while n:
    c = chr(ord('a') + (n % 26) - 1)
    ans = c + ans
    n = n // 26

print(ans)
