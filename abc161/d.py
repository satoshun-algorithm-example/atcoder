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


K = int(input())

count = 0
ans = 0

while count != K:
    ans += 1
    count += check(ans)

print(ans)
