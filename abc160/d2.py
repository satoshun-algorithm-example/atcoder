def line(N, X, Y):
    X = X - 1
    Y = Y - 1

    queue = [(a, a + 1) for a in range(N - 1)]
    queue.append((X, Y))
    visited = set(queue)
    print(len(queue))

    for i in range(N - 2):
        new_queue = []

        def add_to_queue(x, y):
            if y == N or y < 0:
                return
            if x == N or x < 0:
                return
            if x == y:
                return

            if x > y:
                x, y = y, x

            t = (x, y)
            if t not in visited:
                new_queue.append(t)
                visited.add(t)

        for q in queue:
            add_to_queue(q[0], q[1] + 1)
            add_to_queue(q[0], q[1] - 1)
            add_to_queue(q[0] + 1, q[1])
            add_to_queue(q[0] - 1, q[1])

        print(len(new_queue))
        # print(f"{len(new_queue)} {new_queue}")
        queue = new_queue


N, X, Y = map(int, input().split())
line(N, X, Y)

# line(5, 2, 4)
# print()
# line(3, 1, 3)
# print()
# line(7, 3, 7)
# print()
# line(10, 4, 8)
