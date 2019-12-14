def main():
    n = int(input())
    values = [int(input()) for _ in range(n)]
    values.sort()

    duplicated = None
    for i in range(n - 1):
        if values[i] == values[i + 1]:
            duplicated = values[i]
            break

    if duplicated is None:
        print("Correct")
        return

    removed = None
    values = set(values)
    for i in range(1, n + 1):
        if i not in values:
            removed = i
            break

    print(str(duplicated) + " " + str(removed))


main()
