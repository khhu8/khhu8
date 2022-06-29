data = [x for x in input().strip()]
data.insert(0, data[1])
data.pop(2)
if len(data) > 3:
    if data[3] == '+' or data[3] == '-':
        data.insert(0, data[3])
        data.pop(4)
    else:
        data.insert(2, data[3])
        data.pop(4)
if len(data) > 5:
    if data[5] == '+' or data[5] == '-':
        data.insert(0, data[5])
        data.pop(6)
    else:
        data.insert(5, data[5])
        data.pop(6)
print(''.join(data))