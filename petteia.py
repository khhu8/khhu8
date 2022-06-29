fin = open('Petteia.in', 'r')
O_input = [int(x) for x in fin.readline().split(', ')]
O_count = O_input[0]
O_input.pop(0)
O_data = []
for i in range(1 , O_count*2, 2):
    temp = O_input[i-1:i+1]
    O_data.append(temp)
X_input = [int(x) for x in fin.readline().split(', ')]
X_count = X_input[0]
X_input.pop(0)
X_data = []
for i in range(1 , X_count*2, 2):
    temp = X_input[i-1:i+1]
    X_data.append(temp)
time = 5
X = []
output = [[[] for _ in range(X_count)], [[] for _ in range(X_count)], [[] for _ in range(X_count)], [[] for _ in range(X_count)], [[] for _ in range(X_count)]]
while time:
    X.append([int(x) for x in fin.readline().split(',')])
    for i in range(len(X_data)):
        if X[5-time][0] == X_data[i][0] and (X_data[i][1] + 2) == X[5-time][1]:
            output[5-time][i] = ([X[5-time][1]+1, X[5-time][1], '1'])
        elif X[5-time][0] == X_data[i][0] and (X_data[i][1] - 2) == X[5-time][1]:
            output[5-time][i] = ([X[5-time][1]-1, X[5-time][1], '2'])
        elif X[5-time][1] == X_data[i][1] and (X_data[i][0] + 2) == X[5-time][0]:
            output[5-time][i] = ([X[5-time][0]+1, X[5-time][1], '3'])
        elif X[5-time][1] == X_data[i][1] and (X_data[i][0] - 2) == X[5-time][0]:
            output[5-time][i] = ([X[5-time][0]-1, X[5-time][1], '4'])
        else:
            output[5-time][i] = 'None'
    time -= 1
print(output)
