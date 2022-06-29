inputarray = input().split(', ')
row1, row2, row3, row4 = inputarray[0].zfill(4), inputarray[1].zfill(4), inputarray[2].zfill(4), inputarray[3].zfill(4)
row1, row2, row3, row4 = [int(x) for x in row1], [int(x) for x in row2], [int(x) for x in row3], [int(x) for x in row4]
array = [row1] + [row2] + [row3] + [row4]

for z in range(5):
    temparray = array
    start = list(map(int, input().split(', ')))
    x, y = start[0], start[1]
    for i in range(6):
        if temparray[x-1][y-1] == 0:
            temparray[x-1][y-1] += 1
            x = (x+1)
            if x == 5:
                x = 1
            print('used 0', x, y)
        elif temparray[x-1][y-1] == 1:
            temparray[x-1][y-1] += 1
            x = (x-1)
            if x == 0:
                x = 4
            print('used 1', x, y)
        elif temparray[x-1][y-1] == 2:
            temparray[x-1][y-1] += 1
            y = (y+1)
            if y == 5:
                y = 1
            print('used 1', x, y)
        elif temparray[x-1][y-1] == 2:
            temparray[x-1][y-1] += 1
            y = (y-1)
            if y == 0:
                y = 4
            print('used 3', x, y)

    print(str(x) + ', ' + str(y))