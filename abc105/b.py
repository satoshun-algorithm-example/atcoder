def cracker(n):
    i = 0
    while True:
        r = (n - i * 4)
        if r < 0:
            print('No')
            return
        if (n - i * 4) % 7 == 0:
            print('Yes')
            return
        i += 1
n = int(input())
cracker(n)
