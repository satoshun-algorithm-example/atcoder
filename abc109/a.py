def abc333(a, b):
    if a * b % 2 == 0:
        return 'No'
    return 'Yes'

a, b = map(int, input().split())
print(abc333(a, b))
