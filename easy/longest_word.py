import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    longest = ''

    for word in line.split(' '):
        if len(word) > len(longest):
            longest = word

    sys.stdout.write(longest)

    if i != len(lines) - 1:
        sys.stdout.write('\n')