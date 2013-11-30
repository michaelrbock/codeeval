import sys
import copy

# recursive function, returns int
# location = [row, col]
def robot_movements(location, visited):
    # base case, already visited
    if tuple(location) in visited:
        return 0
    # base case, at final destination
    if tuple(location) == (3, 3):
        return 1

    # keep track of where we've been
    new_visited = copy.deepcopy(visited)
    new_visited[tuple(location)] = True
    sum = 0

    # recurse on all possible directions
    # UP
    new_loc = [location[0] - 1, location[1]]
    if new_loc[0] >= 0:
        sum += robot_movements(new_loc, new_visited)
    # DOWN
    new_loc = [location[0] + 1, location[1]]
    if new_loc[0] <= 3:
        sum += robot_movements(new_loc, new_visited)
    # RIGHT
    new_loc = [location[0], location[1] + 1]
    if new_loc[1] <= 3:
        sum += robot_movements(new_loc, new_visited)
    # LEFT
    new_loc = [location[0], location[1] - 1]
    if new_loc[1] >= 0:
        sum += robot_movements(new_loc, new_visited)

    return sum

starting_location = [0,0]
visited = {}
possible_ways = robot_movements(starting_location, visited)
sys.stdout.write(str(possible_ways))
