import sys

input = open(sys.argv[1], 'r')

lines = []

for l in input:
    lines.append(l.split(' '))

input.close()