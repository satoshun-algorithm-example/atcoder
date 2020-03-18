# https://atcoder.jp/contests/abc158/tasks/abc158_d

S = input()
Q = int(input())

elements = [None for _ in range(Q * 2 + len(S) * 2)]

head = Q + len(S)
last = len(S)
for i, s in enumerate(S):
    elements[head + i] = s

for _ in range(Q):
    query = input()
    if query[0] == '1':
        elements[head:head + last] = elements[head + last - 1:head - 1:-1]
    else:
        if query[2] == '1':
            head -= 1
            elements[head] = query[4]
        else:
            elements[head + last] = query[4]

        last += 1

elements = filter(lambda a: a is not None, elements)
print(''.join(elements))
