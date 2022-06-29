data = input().strip().split(', ')
data = [x.split(' ') for x in data]
list = ['A', 'B', 'C', 'D', 'E']

def POP(type, list, x):
    if type == 'S':
        for i in range(x):
            list.pop()
    elif type == 'Q':
        for i in range(x):
            list = list.pop(0)
    return list
def PSH(list, x):
    list = list.append(x)
    return list
def DUP(list, x):
    list = list.extend(list[0:x])
    return list
def SWP(list, x):
    list[0:x], list[-x:] = list[-x:], list[0:x]
    return list

for i in range(1, len(data)-1):
    if data[i][0] == 'POP':
        list = POP(data[0][0], list, int(data[i][1]))
    elif data[i][0] == 'PSH':
        list = PSH(list, data[i][1])
    elif data[i][0] == 'DUP':
        list = DUP(list, int(data[i][1]))
    elif data[i][0] == 'SWP':
        list = SWP(list, int(data[i][1]))
    elif data[i][0] == 'SWH':
        if data[0][0] == 'S':
            data[0][0] == 'Q'
        else:
            data[0][0] = 'S'

prtlen = int(data[-1][1])
if data[0][0] == 'S':
    print(', '.join(list[-prtlen:]))
else: 
    print(', '.join(list[:prtlen]))