def binary_search(target, remain):
    low = 0
    high = len(target) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = target[mid]
        if guess == remain:
            return mid
        if guess > remain:
            high = mid - 1
        else:
            low = mid + 1

    if target[low] <= remain:
        return low

    if low == 0:
        return None

    if target[low - 1] <= remain:
        return low - 1

    return None


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(1, len(A)):
    A[i] += A[i - 1]

for i in range(1, len(B)):
    B[i] += B[i - 1]

A = [0] + A
B = [0] + B

ans = -1
for i in range(len(A)):
    if A[i] > K:
        break

    g = i
    remain = K - A[i]
    a = binary_search(B, remain)
    if a is not None:
        g += a

    ans = max(ans, g)

print(ans)
