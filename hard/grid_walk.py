import sys

def is_accessible(point):
    total = 0
    for digit in str(point[0]).replace('-', ''):
        total += int(digit)
    for digit in str(point[1]).replace('-', ''):
        total += int(digit)
    return total <= 19

visited = {} # maps tuple of (x,y) to True/False
to_vist = [(0, 0)] # points to explore
current = None # the current location in (x, y)
count = 0 # the number of points accessible

while to_vist:
    current = to_vist.pop(0)
    if current in visited:
        continue
    count += 1
    visited[current] = True
    # UP
    up = (current[0], current[1] - 1)
    if is_accessible(up) and up not in visited:
        to_vist.append(up)
    # DOWN
    down = (current[0], current[1] + 1)
    if is_accessible(down) and down not in visited:
        to_vist.append(down)
    # LEFT
    left = (current[0] - 1, current[1])
    if is_accessible(left) and left not in visited:
        to_vist.append(left)
    # RIGHT
    right = (current[0] + 1, current[1])
    if is_accessible(right) and right not in visited:
        to_vist.append(right)

sys.stdout.write(str(count))
