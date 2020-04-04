# https://atcoder.jp/contests/abc161/tasks/abc161_d
def check(k):
    prev = k % 10
    k //= 10
    while k:
        cur = k % 10
        if abs(cur - prev) > 1:
            return False
        k //= 10
        prev = cur
    return True


hijack = {
    30000: 223221112,
    25000: 111233456,
    20000: 76667876,
    15000: 45544456,
    10000: 22111101,
    5000: 4454545,
    1000: 110111,
    0: 0
}

K = int(input())

count = 0
ans = 0
for (i, j) in hijack.items():
    if K >= i:
        count = i
        ans = j
        break

while count != K:
    ans += 1
    count += check(ans)

print(ans)
