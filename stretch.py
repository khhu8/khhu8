from dataclasses import dataclass


data = [int(x) for x in input().strip().split(' ')]
r, c, s, n = data[0], data[1], data[2], data[3]
blocked = []
for i in range(n):
    blocked.append(data[3 + n])
board = []
for i in range(c*r + 1):
    board.append(i)

result = []
b=1
while b:
    for i in blocked:
        if board[s] != i and board[s+1] != i and board[s+2] != i:
            result.append('A')
            s = board[s+3]
            if (s-1) % c == 0:
                print(''.join(result))
                break
        if board[s] != i and board[s+c] != i and board[s+c+1] != i:
            result.append('B')
            s = board[s+c+2]
            if (s-1) % c == 0:
                print(''.join(result))
                break
        if board[s] != i and board[s+1] != i and board[s+c+1] != i and board[s+2*c+1] != i:
            result.append('C')
            s = board[s+2*c+2]
            if (s-1) % c == 0:
                print(''.join(result))
                break
