import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    for c in line:
        if c.isalpha():
            if c.islower():
                sys.stdout.write(c.upper())
            elif c.isupper():
                sys.stdout.write(c.lower())
        else:
            sys.stdout.write(c)

    if i != len(lines) - 1:
        sys.stdout.write('\n')