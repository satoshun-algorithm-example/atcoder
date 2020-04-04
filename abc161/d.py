# https://atcoder.jp/contests/abc161/tasks/abc161_d
K = int(input())

count = 0
ans = 0

while count != K:
    ans += 1

    # check lunlun
    a = list(map(int, str(ans)))
    is_lunlun = True
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) > 1:
            is_lunlun = False
            break

    count += is_lunlun

print(ans)
