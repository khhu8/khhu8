origstr = [x for x in input() if x.isalpha()]
origstr = [x.lower() for x in origstr]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
templist = []
resultstr = []
while origstr:
    for x in alphabet:
        if x in origstr:
            templist.append(origstr[origstr.index(x)])
            origstr.pop(origstr.index(x))
    templist = sorted(templist)
    resultstr.append(''.join(templist))
    templist = []
    print(resultstr)
print(''.join(resultstr))