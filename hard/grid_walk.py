import sys
from collections import defaultdict, namedtuple

Point = namedtuple('Point', 'x y')

def is_accessible(point):
    total = 0
    for digit in str(point.x).replace('-', ''):
        total += int(digit)
    for digit in str(point.y).replace('-', ''):
        total += int(digit)
    return total <= 19

visited = defaultdict(bool) # maps tuple of (x,y) to True/False
to_vist = [Point(0, 0)] # points to explore
current = None # the current location in (x, y)
count = 0 # the number of points accessible

while to_vist:
    current = to_vist.pop(0)
    if visited[current]:
        continue
    count += 1
    visited[current] = True
    # UP
    up = Point(current.x, current.y - 1)
    if is_accessible(up) and not visited[up]:
        to_vist.append(up)
    # DOWN
    down = Point(current.x, current.y + 1)
    if is_accessible(down) and not visited[down]:
        to_vist.append(down)
    # LEFT
    left = Point(current.x - 1, current.y)
    if is_accessible(left) and not visited[left]:
        to_vist.append(left)
    # RIGHT
    right = Point(current.x + 1, current.y)
    if is_accessible(right) and not visited[right]:
        to_vist.append(right)

sys.stdout.write(str(count))
