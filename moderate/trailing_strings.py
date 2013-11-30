import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    A, B = line.split(',')
    works = True
    j = len(A) - 1
    for c in reversed(B):
        if c != A[j]:
            works = False
            break
        j -= 1
    if works:
        sys.stdout.write('1')
    else:
        sys.stdout.write('0')
    if i != len(lines) - 1:
        sys.stdout.write('\n')
    