"""
Write a program to determine the largest sum of contiguous integers in a list.
"""

import sys

# read in from file
input = open(sys.argv[1], 'r')

lists = []
for line in input:
    lists.append([int(x) for x in line.strip().split(',')])

input.close()

def max_subarray(arr):
    max_ending_here = max_so_far = 0
    for e in arr:
        max_ending_here = max(0, max_ending_here + e)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

for i, lst in enumerate(lists):
    sys.stdout.write(str(max_subarray(lst)))
    if i != len(lists) - 1:
        sys.stdout.write('\n')
