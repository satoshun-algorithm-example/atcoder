def main():
    n = int(input())
    profits = []
    for _ in range(n):
        profits.append(int(input()))

    for i in range(1, len(profits)):
        if profits[i - 1] == profits[i]:
            print('stay')
        elif profits[i - 1] > profits[i]:
            print('down ' + str(profits[i - 1] - profits[i]))
        else:
            print('up ' + str(profits[i] - profits[i - 1]))


main()
