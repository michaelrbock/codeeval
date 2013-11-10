import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

board = []
for i in xrange(256):
    board.append([0]*256)

for i, line in enumerate(lines):
    command = line.split()
    if command[0] == 'SetRow':
        for j in xrange(256):
            board[int(command[1])][j] = int(command[2])
    elif command[0] == 'SetCol':
        for j in xrange(256):
            board[j][int(command[1])] = int(command[2])
    elif command[0] == 'QueryRow':
        sum = 0
        for j in xrange(256):
            sum += board[int(command[1])][j]
        sys.stdout.write(str(sum))
        if i != len(lines) - 1:
            sys.stdout.write('\n')
    elif command[0] == 'QueryCol':
        sum = 0
        for j in xrange(256):
            sum += board[j][int(command[1])]
        sys.stdout.write(str(sum))
        if i != len(lines) - 1:
            sys.stdout.write('\n')
