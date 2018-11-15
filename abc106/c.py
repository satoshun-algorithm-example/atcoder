days = 5000000000000000

s = int(input())
k = int(input())

ss = str(s)
for i in range(len(ss)):
    if ss[i] != "0":
        break
    if k - 1 == i:
        print(1)
        exit(0)

print(str(s)[0])
