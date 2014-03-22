import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    digit_count = {}
    for count in xrange(0,len(line)):
        digit_count[count] = 0

    for d in line:
        if int(d) in digit_count:
            digit_count[int(d)] += 1
        else:
            digit_count[int(d)] = 1

    self_describing = True
    for j, digit in enumerate(line):
        if int(digit) != digit_count[j]:
            self_describing = False

    if self_describing:
        sys.stdout.write('1')
    else:
        sys.stdout.write('0')

    if i != len(lines) - 1:
        sys.stdout.write('\n')
