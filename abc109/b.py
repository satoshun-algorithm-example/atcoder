def shiritori(n, ws):
    if len(ws) != len(set(ws)):
        return 'No'

    for i in range(1, len(ws)):
        if ws[i - 1][-1] != ws[i][0]:
            return 'No'
    return 'Yes'

n = int(input())
ws = []
for _ in range(n):
    ws += [input()]
print(shiritori(n, ws))
