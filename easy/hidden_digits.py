import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    output = ''

    for c in line:
        if c.isdigit():
            output += c
        elif c.isalpha() and c.islower():
            if ord(c) - 97 < 10:
                output += str(ord(c) - 97)

    if output == '':
        sys.stdout.write('NONE')
    else:
        sys.stdout.write(output)

    if i != len(lines) - 1:
        sys.stdout.write('\n')
