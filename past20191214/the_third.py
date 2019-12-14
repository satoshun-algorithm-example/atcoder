def main():
    a, b, c, d, e, f = map(int, input().split())
    print(sorted([a, b, c, d, e, f])[-3])


main()
