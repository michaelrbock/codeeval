import sys

input = open(sys.argv[1], 'r')

lines = []
m = []

for l in input:
    line = l.split(' ')
    m.append(int(line[-1]))
    lines.append(line[:-1])

input.close()

for i in xrange(len(lines)):
    if m[i] > len(lines[i]):
        continue
    sys.stdout.write(lines[i][-m[i]])
    if i != len(lines)-1:
        sys.stdout.write('\n')
