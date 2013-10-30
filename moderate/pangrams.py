"""
You are to write a program, which takes a sentence, 
and returns all the letters it is missing (which 
    prevent it from being a pangram). 
You should ignore the case of the letters in sentence, 
and your return should be all lower case letters, 
in alphabetical order. You should also ignore all non 
US-ASCII characters. In case the input sentence is already 
a pangram, print out the string NULL
"""

import sys

# read in from file
input = open(sys.argv[1], 'r')

lines = []
for line in input:
    lines.append(line.strip())

input.close()

letters = "abcdefghijklmnopqrstuvwxyz"

for i, line in enumerate(lines):
    char_dict = {}
    for char in line:
        if char.isalpha():
            if char.lower() not in char_dict:
                char_dict[char.lower()] = True
    pangram = True
    for char in letters:
        if char not in char_dict:
            sys.stdout.write(char)
            pangram = False
    if pangram:
        sys.stdout.write('NULL')
    if i != len(lines) - 1:
        sys.stdout.write('\n')
