import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    min_coins = 0
    total = int(line)

    while total > 0:
        if total >= 5:
            total -= 5
            min_coins += 1
        elif total >= 3:
            total -= 3
            min_coins += 1
        elif total >= 1:
            total -= 1
            min_coins += 1

    sys.stdout.write(str(min_coins))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
