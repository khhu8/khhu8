line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')
x = max(len(line1), len(line2), len(line3))
for i in range(x - len(line1)):
    line1.append('0')
for i in range(x - len(line2)):
    line2.append('0')
for i in range(x - len(line3)):
    line3.append('0')
line1 = [int(x) for x in line1]
line2 = [int(x) for x in line2]
line3 = [int(x) for x in line3]
result = 0
for i in range(x):
    result += max(line1[i], line2[i], line3[i])

print(result)