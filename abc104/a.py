def rated_for_me(rate):
    if rate < 1200:
        return "ABC"
    if rate < 2800:
        return "ARC"
    return "AGC"

rate = int(input())
print(rated_for_me(rate))
