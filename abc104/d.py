s = input()
leng = len(s)
c = 0
for i in range(leng):
    if s[i] not in 'A?':
        continue
    for j in range(i + 1, leng):
        if s[j] not in 'B?':
            continue
        for k in range(j + 1, leng):
            if s[k] not in 'C?':
                continue
            c += 1
print(c)
