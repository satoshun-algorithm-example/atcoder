def main():
    n = int(input())
    values = []
    duplicated = None
    for _ in range(n):
        v = int(input())
        if v in values:
            duplicated = v
            continue
        values.append(v)

    if duplicated is None:
        print("Correct")
        return

    values = set(values)

    for i in range(1, n + 1):
        if i not in values:
            print(str(duplicated) + " " + str(i))
            return


main()
