import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

for i, line in enumerate(lines):
    rows, cols, nums = line.split(';')
    rows, cols = int(rows), int(cols)
    nums = nums.split()
    arr = []
    for r in xrange(rows):
        arr.append([])
        for c in xrange(cols):
            arr[r].append(nums.pop(0))

    direction = "RIGHT"
    visited = {}
    location = [0, 0]
    print_count = 0

    while (print_count < rows * cols):
        if tuple(location) not in visited:
            sys.stdout.write(arr[location[0]][location[1]])
            sys.stdout.write(' ')
            visited[(location[0], location[1])] = True
            print_count += 1

        if direction == "RIGHT":
            new = (location[0], location[1] + 1)
            if new[1] < len(arr[0]) and new not in visited:
                location[1] += 1
            else:
                direction = "DOWN"
        elif direction == "DOWN":
            new = (location[0] + 1, location[1])
            if new[0] < len(arr) and new not in visited:
                location[0] += 1
            else:
                direction = "LEFT"
        elif direction == "LEFT":
            new = (location[0], location[1] - 1)
            if new[1] >= 0 and new not in visited:
                location[1] -= 1
            else:
                direction = "UP"
        elif direction == "UP":
            new = (location[0] - 1, location[1])
            if new[0] >= 1 and new not in visited:
                location[0] -= 1
            else:
                direction = "RIGHT"

    if i != len(lines) - 1:
        sys.stdout.write('\n')
