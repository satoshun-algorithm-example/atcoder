def main():
    s = input()

    c = 0
    while len(s) >= 2:
        is_match = False

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                s = s[:i] + s[i + 2:]
                c += 2
                is_match = True
                break

        if not is_match:
            break

    print(c)


main()
