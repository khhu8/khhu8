expression = input()
list = []
for x in expression[::-1]:
    if x.isdigit():
        list.append(int(x))
    elif x == ' ':
        next
    else:
        num1 = list.pop()
        num2 = list.pop()
        if x == '+':
            list.append(num1 + num2)
        elif x == '-':
            list.append(num1 - num2)
        elif x == '*':
            list.append(num1 * num2)
        elif x == '/':
            list.append(num1 / num2)   
        elif x == '@':
            num3 = list.pop()
            if num1 > 0:
                list.append(num2)
            else:
                list.append(num3)
print(list.pop())