import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    operators = []
    nums = []
    expression = line.split()
    for e in reversed(expression):
        if e.isdigit():
            nums.append(int(e))
        else:
            operators.append(e)
    while operators:
        operator = operators.pop(0)
        if operator == '+':
            result = nums.pop() + nums.pop()
            nums.append(result)
        elif operator == '*':
            result = nums.pop() * nums.pop()
            nums.append(result)
        elif operator == '/':
            result = nums.pop() / nums.pop()
            nums.append(result)
    sys.stdout.write(str(nums[0]))
    if i != len(lines) - 1:
        sys.stdout.write('\n')
