import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line[:-1]) # strip trailing '\n'

input.close()

for i, line in enumerate(lines):
    S, t = line.split(',')
    reversed_index = S[::-1].find(t)
    if reversed_index == -1:
        sys.stdout.write('-1')
    else:
        sys.stdout.write(str(len(S) - 1 - reversed_index))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
