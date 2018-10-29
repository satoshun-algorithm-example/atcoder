def base2_number(n):
    result = ""
    while True:
        print(n)
        rem = n % 2
        n = n // 2
        result += str(abs(rem))
        if n == 0:
            break
    return int(result)
n = int(input())
print(base2_number(n))
