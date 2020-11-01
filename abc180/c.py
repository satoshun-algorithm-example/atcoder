import heapq

N = int(input())

ans = []

for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        heapq.heappush(ans, i)
        heapq.heappush(ans, N // i)

for i in ans:
    print(i)
