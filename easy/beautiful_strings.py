import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    letters = {}
    for c in line:
        if c.isalpha():
            if c.lower() in letters:
                letters[c.lower()] += 1
            else:
                letters[c.lower()] = 1
    sorted_letters = sorted(letters.iteritems(), key=operator.itemgetter(1), reverse=True)
    sum = 0
    value = 26
    for letter, count in sorted_letters:
        sum += count * value
        value -= 1
    sys.stdout.write(str(sum))
    if i != len(lines) - 1:
        sys.stdout.write('\n')
