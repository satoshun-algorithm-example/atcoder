# https://atcoder.jp/contests/abc158/tasks/abc158_d
from collections import deque

S = input()
Q = int(input())

is_reverse = False
text = deque(S)
for _ in range(Q):
    query = input()
    if query[0] == '1':
        is_reverse = not is_reverse
    else:
        if query[2] == '1':
            if is_reverse:
                text.append(query[4])
            else:
                text.appendleft(query[4])
        else:
            if is_reverse:
                text.appendleft(query[4])
            else:
                text.append(query[4])

if is_reverse:
    print(''.join(text)[::-1])
else:
    print(''.join(text))
