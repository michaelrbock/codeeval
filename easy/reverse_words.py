import sys

input = open(sys.argv[1], 'r')

lines = []

for l in input:
    lines.append(l.strip().split(' '))

input.close()

for j, line in enumerate(lines):
    if line == ['']:
        continue
    for i in xrange(len(line)-1, -1, -1):
        sys.stdout.write(line[i])
        sys.stdout.write(' ')
    if j != len(lines) - 1:
        sys.stdout.write('\n')
