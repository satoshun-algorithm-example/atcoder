def main():
    s = input()

    start = 0
    words = []
    for end in range(1, len(s)):
        if end == start:
            continue

        if s[start].isupper() and s[end].isupper():
            words.append(s[start:end + 1])
            start = end + 1

    print(''.join(sorted(words, key=lambda x: x.lower())))


main()
