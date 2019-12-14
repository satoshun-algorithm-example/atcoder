def main():
    n, q = map(int, input().split())
    followers = [['N'] * n for _ in range(n)]

    for _ in range(q):
        op = input().split()
        if op[0] == '1':
            followers[int(op[1]) - 1][int(op[2]) - 1] = 'Y'
        if op[0] == '2':
            x = int(op[1]) - 1
            for y in range(n):
                if followers[y][x] == 'Y':
                    followers[x][y] = 'Y'
        if op[0] == '3':
            pass
            # for i, f in enumerate(followers[int(op[1]) - 1]):
            #     if f == 'Y':
            #         for j, nf in enumerate(followers[i]):
            #             if nf == 'Y':
            #                 followers[int(op[1]) - 1][j] = 'Y'

    for f in followers:
        print(''.join(f))


main()
