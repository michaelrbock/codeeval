from __future__ import division
import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    lower_count, upper_count = 0, 0

    for letter in line:
        if letter.isalpha():
            if letter.islower():
                lower_count += 1
            elif letter.isupper():
                upper_count += 1
    total = lower_count + upper_count
    lower_percent = (lower_count / total) * 100.0
    upper_percent = (upper_count / total) * 100.0
    sys.stdout.write('lowercase: %.2f uppercase: %.2f' % (lower_percent, upper_percent))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
