from datetime import datetime


def a():
    now = datetime.now()
    for _ in range(10000000):
        a = ord('b') - ord('a')
    print(datetime.now())
    print(now)


def b():
    for _ in range(10000000):
        a = ord('b') - ord('a')


a()
