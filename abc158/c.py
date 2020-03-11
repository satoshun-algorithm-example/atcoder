A, B = map(int, input().split())

a_min = A * 12.5
a_max = a_min + 12.5
a_min = int(a_min)
a_max = int(a_max)

b_min = B * 10.0
b_max = b_min + 10.0
b_min = int(b_min)
b_max = int(b_max)

if b_min <= a_min < b_max:
    print(a_min)
elif a_min <= b_min < a_max:
    print(b_min)
else:
    print(-1)
