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
            y = int(op[1]) - 1
            follower = followers[y].copy()
            for x in range(n):
                if follower[x] == 'Y':
                    y2 = x
                    for x2 in range(n):
                        if followers[y2][x2] == 'Y':
                            followers[y][x2] = 'Y'

    for f in followers:
        print(''.join(f))


main()
