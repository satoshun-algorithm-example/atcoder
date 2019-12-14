def main():
    s = input()

    c = 0
    i = 0
    while len(s) > i + 1:
        if s[i] != s[i + 1]:
            s = s[:i] + s[i + 2:]
            c += 2
            if i != 0:
                i -= 1
            continue
        i += 1

    print(c)


main()
