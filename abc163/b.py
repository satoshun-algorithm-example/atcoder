    N, M = map(int, input().split())
    A = map(int, input().split())

    d = N - sum(A)
    if d < 0:
        print(-1)
    else:
        print(d)
