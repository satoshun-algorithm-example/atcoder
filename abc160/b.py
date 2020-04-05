# https://atcoder.jp/contests/abc160/tasks/abc160_b
X = int(input())
happiness = 0

a = X // 500
X = X % 500
b = X // 5

print(a * 1000 + b * 5)
