def string_transformation(s, t):
    for i in range(len(s)):
        text = s[i]
        textt = t[i]
        for j in range(i, len(s)):
            if text == s[j]:
                if textt != t[j]:
                    return 'No'
            if textt == t[j]:
                if text != s[j]:
                    return 'No'
    return 'Yes'


s = input()
t = input()
print(string_transformation(s, t))
