s = input()
t = input()

ans = sum(s[i] != t[i] for i in range(len(s)))
print(ans)
