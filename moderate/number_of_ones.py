import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    bits = bin(int(line))

    total = 0

    for c in str(bits):
        if c == '1':
            total += 1

    sys.stdout.write(str(total))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
