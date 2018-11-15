days = 5000000000000000

s = int(input())
k = int(input())

ss = str(s)
for i in range(len(ss)):
    if ss[i] != "1":
        print(ss[i])
        break
    if k - 1 == i:
        print(1)
        break
