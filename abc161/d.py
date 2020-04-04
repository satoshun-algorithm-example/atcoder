# https://atcoder.jp/contests/abc161/tasks/abc161_d
K = int(input())

count = 0
ans = 0
while True:
    if count == K:
        break

    ans += 1

    # check lunlun
    a = list(map(int, str(ans)))
    if len(a) == 1:
        count += 1
        continue

    is_lunlun = True
    for i in range(len(a)):
        if i == 0:
            if abs(a[i] - a[i + 1]) > 1:
                is_lunlun = False
                break
        elif i == len(a) - 1:
            if abs(a[i] - a[i - 1]) > 1:
                is_lunlun = False
                break
        else:
            if abs(a[i] - a[i + 1]) > 1:
                is_lunlun = False
                break
            if abs(a[i] - a[i - 1]) > 1:
                is_lunlun = False
                break

    count += is_lunlun

print(ans)
