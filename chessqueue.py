data = input().split(', ')
x, y, n = int(data[0]), int(data[1]), int(data[2])
result = 24 - 8 * n

possible = []
for i in range(1, n + 1):
    possible.append([x, y-1])
    possible.append([x+1, y-1])
    possible.append([x+1, y+1])
    possible.append([x+1, y])
    possible.append([x-1, y-1])
    possible.append([x-1, y+1])
    possible.append([x-1, y])
    possible.append([x, y+1])

for each in possible:
    if each[0] > 5 or each[1] > 5 or each[0] < 1 or each[1] < 1:
        result += 1

print(result)