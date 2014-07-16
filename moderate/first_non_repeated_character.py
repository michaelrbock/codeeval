import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    count = {}
    for char in line:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in line:
        if count[char] == 1:
            sys.stdout.write(char)
            break

    if i != len(lines) - 1:
        sys.stdout.write('\n')
