import sys

# read in from file
input = open(sys.argv[1], 'r')

numbers = []
for line in input:
    numbers.append(line)

input.close()

for i, number in enumerate(numbers):
    sum = 0
    for digit in number:
        if digit.isdigit():
            sum += int(digit)
    sys.stdout.write(str(sum))
    if i != len(numbers) - 1:
        sys.stdout.write('\n')
