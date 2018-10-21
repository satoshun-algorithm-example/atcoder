def rotation(s, t):
    l = len(s)
    j = 0
    while True:
        jj = True
        for i in range(len(s)):
            if s[(i + j) % l] != t[i]:
                jj = False
                break
        if jj:
            return 'Yes'
        j += 1
        if j == l:
            break
    return 'No'

s = input()
t = input()

print(rotation(s, t))
