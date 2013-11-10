import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    words = []
    numbers = []
    for element in line.split(','):
        if element.isdigit():
            numbers.append(element)
        else:
            words.append(element)
    for j, word in enumerate(words):
        sys.stdout.write(word)
        if j != len(words) - 1:
            sys.stdout.write(',')
    if words and numbers:
        sys.stdout.write('|')
    for j, number in enumerate(numbers):
        sys.stdout.write(number)
        if j != len(numbers) - 1:
            sys.stdout.write(',')
    if i != len(lines) - 1:
        sys.stdout.write('\n')
