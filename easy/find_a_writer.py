import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    code, key = line.split('|')
    key = key.strip()
    key = [int(x) for x in key.split(' ')]

    output = ''

    for num in key:
        output += code[num-1]

    sys.stdout.write(output)

    if i != len(lines) - 1:
        sys.stdout.write('\n')
