import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    nums = line.split(' ')
    nums = [float(x) for x in nums]

    nums = sorted(nums)

    for j, num in enumerate(nums):
        sys.stdout.write(str(num))
        if j != len(nums) - 1:
            sys.stdout.write(' ')

    if i != len(lines) - 1:
        sys.stdout.write('\n')
