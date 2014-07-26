import sys

input_file = open(sys.argv[1], 'r')

def location_or_none(grid, i, j):
    if i >= 0 and i < len(grid):
        if j >= 0 and j < len(grid[i]):
            return grid[i][j]

for line in input_file:
    # M = number of rows, N = number of cols
    meta, blank_data = line.split(';')
    M, N = map(int, meta.split(','))

    count = 0
    grid = [] # list of lists
    for i in range(M):
        grid.append([])
        for j in range(N):
            grid[i].append(blank_data[count])
            count += 1

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == '.':
                # 1 2 3
                # 4 X 5
                # 6 7 8
                mines = 0
                if location_or_none(grid, i-1, j-1) == '*':
                    mines += 1
                if location_or_none(grid, i-1, j) == '*':
                    mines += 1
                if location_or_none(grid, i-1, j+1) == '*':
                    mines += 1
                if location_or_none(grid, i, j-1) == '*':
                    mines += 1
                if location_or_none(grid, i, j+1) == '*':
                    mines += 1
                if location_or_none(grid, i+1, j-1) == '*':
                    mines += 1
                if location_or_none(grid, i+1, j) == '*':
                    mines += 1
                if location_or_none(grid, i+1, j+1) == '*':
                    mines += 1

                grid[i][j] = str(mines)

    output = ''
    for row in grid:
        output += ''.join(row)
    print output

input_file.close()