def main():
    n = int(input())
    rests = list(map(int, input().split()))
    q = int(input())

    cards = 0
    for _ in range(q):
        query = input()

        if query[0] == '1':
            query = query.split()
            index = int(query[1]) - 1
            num = int(query[2])
            if rests[index] >= num:
                cards += num
                rests[index] -= num

        if query[0] == '2':
            query = query.split()
            num = int(query[1])

            # check
            is_ok = True
            for i in range(0, n, 2):
                if rests[i] < num:
                    is_ok = False
                    break

            if not is_ok:
                continue

            for i in range(0, n, 2):
                rests[i] -= num
                cards += num

        if query[0] == '3':
            query = query.split()
            num = int(query[1])

            # check
            is_ok = True
            for i in range(n):
                if rests[i] < num:
                    is_ok = False
                    break

            if not is_ok:
                continue

            for i in range(n):
                rests[i] -= num
                cards += num

    print(cards)


main()
