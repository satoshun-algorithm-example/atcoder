def main():
    n = int(input())
    values = [int(input()) for _ in range(n)]
    values.sort()
    se = set(values)

    if len(se) == len(values):
        print("Correct")
        return

    removed = None
    for i in range(n):
        if values[i] != i + 1:
            removed = i + 1
            break

    for i in range(n - 1):
        if values[i] == values[i + 1]:
            print(str(values[i + 1]) + " " + str(removed))
            return


main()
