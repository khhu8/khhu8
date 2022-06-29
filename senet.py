data = list(map(int, input().strip().split(', ')))
bcount = data[0]
bdata = data[1:bcount+1]
wcount, wdata = data[bcount+1], data[bcount+2:-1]
rodcount = data[-1]
if (data[1] + rodcount) in bdata:
    print("CANNOT MOVE")
elif data[1] + rodcount > 31:
    print("CANNOT MOVE")
elif data[1] + rodcount == 31:
    print("DONE")
elif data[1] + rodcount > 26 and data[1] <= 26:
    print("26")
elif data[1] + rodcount == 27 and 15 not in bdata:
    print("15")
else:
    print(str(data[1] + rodcount))