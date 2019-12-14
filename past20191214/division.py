def main():
    n = int(input())
    hapinnes = []
    for _ in range(n - 1):
        h = list(map(int, input().split()))
        diff = n - len(h)
        hapinnes.append(([0] * diff) + h)

    a, b, c = [], [], []

    def calculate(pair):
        result = 0
        for i in range(len(pair)):
            for j in range(i + 1, len(pair)):
                result += hapinnes[pair[i]][pair[j]]

        return result

    m = 0

    def add(i):
        nonlocal m

        if i == n:
            m = max(m, calculate(a) + calculate(b) + calculate(c))
            return

        a.append(i)
        add(i + 1)
        a.pop()

        b.append(i)
        add(i + 1)
        b.pop()

        c.append(i)
        add(i + 1)
        c.pop()

    add(0)

    print(m)


main()
