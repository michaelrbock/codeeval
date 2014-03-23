import sys
import operator
import json

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    j = json.loads(line)

    total = 0

    for item in j['menu']['items']:
        if item: # check that it's not None
            if 'label' in item:
                total += int(item['id'])

    sys.stdout.write(str(total))

    if i != len(lines) - 1:
        sys.stdout.write('\n')
