data = [[], [], [], [], []]
list = [4] * 12
for i in range(5):
    data[i] = [int(x) for x in input() if x.isnumeric()]

for n in range(5):
    start = (data[n-1][0] - 1)
    if n // 2 == 0 and list[start] <= 6 and list[start + range(list[start])] > 6: 
        for x in range(list[start] - 1):
            list[(start + x) // 12] += 1
    elif n // 2 == 1 and list[start] <= 12 and list[start + range(list[start])] <= 6:
        for x in range(list[start] - 1):
            list[(start + x) // 12] += 1
    else:
        for x in range(list[start]):
            list[(start + x) // 12] += 1
        list[start] = 0
        print(list[data[n][1] - 1])

