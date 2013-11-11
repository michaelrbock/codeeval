import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i,  line in enumerate(lines):
    nums = [int(x) for x in line.split()]
    n = nums.pop(0)
    diffs = {}
    for j in xrange(1, len(nums)):
        diff = abs(nums[j] - nums[j-1])
        if diff not in diffs:
            diffs[diff] = True
    jolly = True
    for j in xrange(1, len(nums)):
        if j not in diffs:
            jolly = False
    if jolly:
        sys.stdout.write('Jolly')
    else:
        sys.stdout.write('Not jolly')
    if i != len(lines) - 1:
        sys.stdout.write('\n')
