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




main()
