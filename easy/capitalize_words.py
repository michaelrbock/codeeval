import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    sys.stdout.write(' '.join(word[0].upper() + word[1:] for word in line.split()))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
