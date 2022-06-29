data = input().split(', ')
string = [x for x in data[0]]
multmatrix = [int(data[1]), int(data[2]), int(data[3]), int(data[4])]
length = -1 * (-len(string) // 2)
matrix = []
for i in range(length):
    matrix.append([0, 0])
newmatrix = []
for i in range(length):
    newmatrix.append([0, 0])

for i in range(len(string)):
    if string[i] == ' ':
        string[i] = 27
    else:
        string[i] = ord(string[i]) - 64

t = 0
for i in range(length):
    matrix[i][0] = string[t]
    try: 
        matrix[i][1] = string[t+1]
    except IndexError:
        continue
    t += 2
if matrix[-1][1] == 0:
    matrix[-1][1] = 27

for i in range(length):
    newmatrix[i][0] = matrix[i][0] * multmatrix[0] + matrix[i][1] * multmatrix[1]
    newmatrix[i][1] = matrix[i][0] * multmatrix[2] + matrix[i][1] * multmatrix[3]
print(newmatrix)
output = []
for i in range(length):
    output.append(newmatrix[i][0] % 27 + 64)
    output.append(newmatrix[i][1] % 27 + 64)
print(output)
for i in range(len(output)):
    if output[i] == 91:
        output[i] = ' '
    else:
        output[i] = chr(output[i])

print(''.join(output))