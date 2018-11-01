def train(n, i):
    return n - i + 1

n, i = map(int, input().split())
print(train(n, i))
