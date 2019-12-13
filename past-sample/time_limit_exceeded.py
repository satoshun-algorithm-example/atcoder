def main():
    n, t = map(int, input().split())
    courses = []
    for _ in range(n):
        a, b = map(int, input().split())
        courses.append([a, b])

    courses = sorted(courses)
    for course in courses:
        if course[1] <= t:
            print(course[0])
            return

    print('TLE')


main()
