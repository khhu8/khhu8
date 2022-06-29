data = input().split(', ')
on = []
for i in range(1, int(data[0]) + 1):
    data[i] = [m for m in data[i]]
    for j in range(1, len(data[i])):
        on.append([int(data[i][0]), int(data[i][j])])
start = [int(t) for t in data[-1]]
x, y = start[0], start[1]
flip = [[x, y], [x+1, y], [x-1, y], [x, y+1], [x, y-1], [x+1, y-1], [x-1, y+1], [x+1, y+1], [x-1, y-1], [x+2, y], [x-2, y], [x, y+2], [x, y-2]]
result = 13
for each in flip:
    if each in on:
        result -= 1
print(result)