def main():
    n = int(input())
    values = [int(input()) for _ in range(n)]
    values.sort()

    removed = None
    for i in range(n):
        if values[i] != i + 1:
            removed = i + 1
            break

    if removed is None:
        print("Correct")
        return

    for i in range(n - 1):
        if values[i] == values[i + 1]:
            print(str(values[i]) + " " + str(removed))
            return


main()
