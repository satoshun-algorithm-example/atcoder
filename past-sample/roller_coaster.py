n, k = map(int, input().split())
heights = map(int, input().split())

print(len([1 for height in heights if height >= k]))
