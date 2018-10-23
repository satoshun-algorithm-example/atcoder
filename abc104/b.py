import string

def accepted(s):
    if s[0] != 'A':
        return "WA"
    if s[1] == 'C':
        return "WA"
    if s[-1] == 'C':
        return "WA"
    c = 0
    for ss in s[1:]:
        if ss == 'C':
            c += 1
        elif ss not in string.ascii_lowercase:
            return "WA"
    if c != 1:
        return "WA"
    return "AC"

s = input()
print(accepted(s))
