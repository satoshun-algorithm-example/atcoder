def base2_number(n):
    result = ""
    while True:
        rem = n % 2
        if rem:
            n -= 1
        n = n // -2
        result += str(abs(rem))
        if n == 0:
            break
    return int(result[::-1])
n = int(input())
print(base2_number(n))
