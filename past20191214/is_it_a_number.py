def main():
    s = input()

    digits = '0123456789'
    for c in s:
        if c not in digits:
            print('error')
            return

    print(int(s) * 2)


main()
