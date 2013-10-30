"""
Given a string write a program to convert it into lowercase.
"""

import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    sys.stdout.write(line.lower())

input.close()
