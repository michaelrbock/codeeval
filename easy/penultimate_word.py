import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    sys.stdout.write(line.split(' ')[len(line.split())-2])

    if i != len(lines) - 1:
        sys.stdout.write('\n')
