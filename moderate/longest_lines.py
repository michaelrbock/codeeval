"""
Write a program to read a multiple line text file and write the 
'N' longest lines to stdout. 
Where the file to be read is specified on the command line.
"""

import sys
import operator

# read in from file
input = open(sys.argv[1], 'r')

num = int(input.readline())

lines = []
for line in input:
    lines.append(line.strip())

input.close()

lines_dict = {} # int (index in lines list): int (length of ith line)

for i, line in enumerate(lines):
    lines_dict[line] = len(line)

sorted_lines = sorted(lines_dict.iteritems(), key=operator.itemgetter(1), reverse=True)

for i in range(num):
    sys.stdout.write(sorted_lines[i][0])
    if i != num - 1:
        sys.stdout.write('\n')
